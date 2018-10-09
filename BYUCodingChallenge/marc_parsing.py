from collections import OrderedDict
import requests
import io
import re
from datetime import datetime
import os
import copy

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

class MARCRecord():
    """Representation of MARC Record"""

    def __init__(self, marc_string):
        self.marc_string = marc_string
    
    def parse_fields(self, fields_to_parse_OrderedDict):
        """Parse record for fields present in OrderedDict
        Returns OrderedDict with field key:value pairs
        """
        fields_storage = copy.deepcopy(fields_to_parse_OrderedDict)
        tags_list = re.split(r"\n(?=\d{3})", self.marc_string)
        for element in tags_list:
            line_id = str(element[:3])
            if fields_to_parse.get(line_id):
                # two dots used to capture "indicator values" defined in MARC standard
                subfields = re.split(r"(?<=^\d{3})\s+..\s+", element, maxsplit=1,flags=re.MULTILINE)
                subfields_split = re.split(r"\n\s+(?=\$. )", subfields[-1])
                for field in subfields_split:
                    subfield_id = field[:2]
                    if subfield_id in fields_to_parse.get(line_id):
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

def get_most_recent_date(list_of_dates):
    """Takes list of dates formatted yyyymmdd"""
    return max(list_of_dates)

def format_date(date_yyyymmdd):
    """Returns ISO 8601 format yyyy-mm-dd"""
    return datetime.strptime(date_yyyymmdd, "%Y%m%d").date().isoformat()

def get_ordered_tag_content(marc_orderedDict):
    """Takes orderedDict of marc tags, returns list of ordered content"""
    retrieved_tags = []
    for field_id in marc_orderedDict.values():
        for subValue in field_id.values():
            for element in subValue:
                retrieved_tags.append(element)
    return retrieved_tags
    
def print_out_tags(tags_list, delimiter="|", filepath=""):
    """Outputs delimited tag string to screen and filepath(if provided)"""
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
marc_instance = MARCRecord(marc_text)
parsed_marc_fields = marc_instance.parse_fields(fields_to_parse)

most_recent = get_most_recent_date(parsed_marc_fields['583']['$c'][:])
formatted_date = format_date(most_recent)
parsed_marc_fields['583']['$c'] = [formatted_date]

retrieved_tags_to_print = get_ordered_tag_content(parsed_marc_fields)
print_out_tags(retrieved_tags_to_print, filepath='output.txt')