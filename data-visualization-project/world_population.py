import json

#Custom modules
from country_codes import get_country_code

#Load the data into a list
filename = 'C:/Users/Copy/Documents/DevCampPythonWorkSpace/data-visualization-project/population_data.json'
with open(filename) as f_obj:
    pop_data = json.load(f_obj)

#Print the 2010 population for each country
for pop_dict in pop_data:
    if pop_dict["Year"] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            print(country_name + ": " + str(population))
        else:
            print('Error - ' + country_name)


