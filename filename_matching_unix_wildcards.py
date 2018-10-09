import fnmatch
import os
def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, "hello*world.py"):
            print("Text files: ", file)

list_files()

user = {
    "name": "John"
}

user2 = {
    "name": "John"
}

if user == user2:
    print("Match!")
else:
    print("Fail")