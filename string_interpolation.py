name = "Kristine"

#f string format
#accepts variables or even basic code like 2+2
greeting = f'Hi {name}'
print(greeting)

#format method
age = 12
product ="Python eLearning Course"

#can't accept the variable directly, must reference the index
greeting2 = "\nSubject: {2}\nHi {0} you are listed as {1} years old and you have purchased: {2}".format(name,age,product)

print(greeting2)