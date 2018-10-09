from collections import OrderedDict
import requests
import io
import re
from datetime import datetime

#TODO Get user input 
#TODO validate user input
#TODO request url
#TODO parse response.content
#TODO return most recent 583 tag
#TODO format 583 tag with different date format
#TODO output delimited string to console and/or file

def generate_url():
    """Asks user for key, returns url"""
    while True:
        resource_key = input("Please enter numeric key for MARC record: ")
        try:
            formatted_key = int(resource_key)
        except:
            print("Invalid input, please ensure key is an integer value")
        else:
            url = f'https://search.lib.byu.edu/marcrecord/bib/{formatted_key}'
            return url

def retrieve_MARC_record(url):
    """Takes in url to MARC record, returns text of MARC record"""
    r = requests.get(url)
    return r.text

url = generate_url()
MARC_body = retrieve_MARC_record(url)

fields_to_parse = OrderedDict([('245', {'$a'}),('100', {'$a'}),('583', {'$c'})])
fields_storage = fields_to_parse.copy()
# print(fields_to_parse['100'])
# for key,value in fields_to_parse.items():
#     print("Key is: " + key)
#     print("Value is: " + value)

def parse_fields(MARC_string, fields_OrderedDict):
    return null

tags_list = re.split(r"\n(?=\d{3})", MARC_body)
for element in tags_list:
    line_id = str(element[:3])
    if fields_to_parse.get(line_id):
        subfields = re.split(r"(?<=^\d{3})\s+..\s+", element, maxsplit=1,flags=re.MULTILINE)
        subfields_split = re.split(r"\n\s+(?=\$. )", subfields[-1])
        for field in subfields_split:
            subfield_id = field[:2]
            if subfield_id in fields_to_parse.get(line_id):
                subfield_content = field[3:]
                if type(fields_storage[line_id]) is OrderedDict:
                    if subfield_id in fields_storage[line_id]:
                        fields_storage[line_id][subfield_id].append(subfield_content)
                    else:
                        fields_storage[line_id][subfield_id] = [subfield_content]
                else: 
                    fields_storage[line_id] = OrderedDict([(subfield_id, [subfield_content])])

for key, value in fields_storage.items():
    print (f"key: {key}")
    for subKey, subValue in value.items():
        print(f'{subKey}: {subValue}')


most_recent = max(fields_storage['583']['$c'])
formatted_date = datetime.strptime(most_recent, "%Y%m%d").date().isoformat()
fields_storage['583']['$c'] = [formatted_date]

retrieved_tags_to_print = []
for field_id in fields_storage.values():
    for subValue in field_id.values():
        for element in subValue:
            retrieved_tags_to_print.append(element)

def print_out_tags(tags_list, delimiter="|", filepath=""):
    tags_string = delimiter.join(tags_list)
    tags_string += delimiter
    if filepath == "":
        print(tags_string)

print_out_tags(retrieved_tags_to_print)


# for tag in tags_list:
#     print("\nNew Line:\n" + tag)

# with io.StringIO(MARC_body) as file_object:
#     lines = file_object.readlines()
# print(lines)



