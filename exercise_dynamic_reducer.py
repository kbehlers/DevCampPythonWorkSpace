"""Function to take in the main mathematical operators as a string ,
take in a list of values,
perform the operation on the elements of the list
"""

#https://www.python-course.eu/python3_lambda.php has good examples of lambda paired with reduce

import operator
from functools import reduce

def dynamic_reducer(list_of_values, operator_as_string):
    operator_function = None
    if operator_as_string == "+":
        operator_function = (lambda a,b: operator.add(a,b))
        
    elif operator_as_string == "-":
        operator_function = lambda a,b: operator.sub(a,b)

    elif operator_as_string == "*":
        operator_function = lambda a,b: operator.mul(a,b)

    elif operator_as_string == "/":
        operator_function = lambda a,b: operator.truediv(a,b)

    else:
        return("invalid operator")

    return (reduce(operator_function,list_of_values))



result = dynamic_reducer([1,2,3], "+")
print(result)


#Solution below is from the video
#Uses almost entirely "functional" programming
# import operator
# from functools import reduce

# def dynamic_reducer(collection, op):
        #defines a dictionary to perform lookups against
        #the operator as a string has a value of a function from the 'operator' library
#     operators = {
#         "+": operator.add,
#         "-": operator.sub,
#         "*": operator.mul,
#         "/": operator.truediv,
#     }

#     return reduce((lambda total, element: operators[op](total, element)), collection)


# total = dynamic_reducer([1, 2, 3], '/')

# print(total)
