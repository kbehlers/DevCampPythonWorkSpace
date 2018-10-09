
with open('output.txt', 'w+') as file_object:
    for value in range(0,1000):
        file_object.write(str(value) + "\n")
        