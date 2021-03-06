from collections import OrderedDict
import requests
import io
import re
from datetime import datetime
import os
import copy

#--FUNCTION DEFINITIONS--
def generate_BYU_url():
    """Asks user for key, returns url string"""
    while True:
        resource_key = input("Please enter numeric key for MARC record: ")
        try:
            formatted_key = int(resource_key)
        except:
            print("Invalid input, please ensure key is an integer value")
        else:
            url = f'https://search.lib.byu.edu/marcrecord/bib/{formatted_key}'
            return url

def retrieve_MARC_text(url):
    """Takes in url to MARC record, returns MARC record as string
        Requires requests library"""
    r = requests.get(url)
    return r.text

def get_most_recent_date(list_of_dates):
    """Takes list of dates formatted yyyymmdd"""
    return max(list_of_dates)

def format_date(date_yyyymmdd):
    """Returns ISO 8601 format yyyy-mm-dd"""
    return datetime.strptime(date_yyyymmdd, "%Y%m%d").date().isoformat()


#--CLASS DEFINITIONS--
class MARCRecord():
    """Representation of MARC Record"""

    def __init__(self, marc_string, fields_to_parse_OrderedDict):
        self.marc_string = marc_string
        self.fields_to_parse_OrderedDict = fields_to_parse_OrderedDict
        self.parsed_marc = self.parse_fields(self.fields_to_parse_OrderedDict)
    
    def parse_fields(self, fields_to_parse_OrderedDict):
        """Parse record for fields present in OrderedDict
        Returns OrderedDict with field key:value pairs
        """
        fields_storage = copy.deepcopy(fields_to_parse_OrderedDict)
        tags_list = re.split(r"\n(?=\d{3})", self.marc_string)
        for element in tags_list:
            line_id = str(element[:3])
            if fields_storage.get(line_id):
                # two dots used to capture "indicator values" defined in MARC standard
                subfields = re.split(r"(?<=^\d{3})\s+..\s+", element, maxsplit=1,flags=re.MULTILINE)
                subfields_split = re.split(r"\n\s+(?=\$. )", subfields[-1])
                for field in subfields_split:
                    subfield_id = field[:2]
                    if subfield_id in fields_storage.get(line_id):
                        subfield_content = field[3:]
                        #Relies on passed dictionary being 'key:value' being 'id: SET of subfields'
                        if type(fields_storage[line_id]) is OrderedDict:
                            if subfield_id in fields_storage[line_id]:
                                fields_storage[line_id][subfield_id].append(subfield_content)
                            else:
                                fields_storage[line_id][subfield_id] = [subfield_content]
                        else: 
                            fields_storage[line_id] = OrderedDict([(subfield_id, [subfield_content])])
        return fields_storage

    def get_ordered_tag_content(self):
        """Returns list of currently parsed fields for the object (defaults defined at object instantiation)"""
        retrieved_tags = []
        for field_id in self.parsed_marc.values():
            for subValue in field_id.values():
                for element in subValue:
                    retrieved_tags.append(element)
        return retrieved_tags

    def print_tags_delimited(self, delimiter="|", filepath=""):
        """Outputs currently parsed fields to screen and filepath(if provided) as delimited string"""
        tags_list = self.get_ordered_tag_content()
        tags_string = delimiter.join(tags_list)
        tags_string += delimiter
        if filepath == "":
            print(tags_string)
        else:
            try:
                with open(filepath, 'w') as file_object:
                    file_object.write(tags_string) 
            except FileNotFoundError:
                print("Invalid file path")
                print(tags_list)
            except:
                print("Unknown error, without filepath arg")
                print(tags_list)
            else:
                print(f'File created at: {os.path.abspath(filepath)}')
                print(tags_string)


#Ordered dictionary where keys are numeric tags and values are SETS of subfield tags
fields_to_parse = OrderedDict([('245', {'$a'}),('100', {'$a'}),('583', {'$c'})])
url = generate_BYU_url()

marc_text = retrieve_MARC_text(url)
marc_instance = MARCRecord(marc_text, fields_to_parse)

most_recent = get_most_recent_date(marc_instance.parsed_marc['583']['$c'][:])
formatted_date = format_date(most_recent)
marc_instance.parsed_marc['583']['$c'] = [formatted_date]

marc_instance.print_tags_delimited(filepath='output.txt')