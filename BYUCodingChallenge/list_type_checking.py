from collections import OrderedDict

fields_to_parse = OrderedDict([('245', {'$a'}),('100', {'$a'}),('583', {'$c'})])
fields_storage = fields_to_parse.copy()

print(type(fields_storage['245']))
fields_storage['245'] = ['$a']
print(type(fields_storage['245']))
if type(fields_storage['245']) is list:
    print("YOU FOUND A LIST")