#Not implementing in class for simplification

def someGenerator():
    counter = 0
    while True:
        if counter < 10:
            #next() will yield at the yield statement and return the value to the caller
            yield counter
            #subsequent next() will run the code after yield up until another yield is encountered
            counter += 1
        else:
            counter = 0
        
        


gen = someGenerator()

print(next(gen)) #0
print(next(gen)) #1
print(next(gen)) #2
print(next(gen)) #3
print(next(gen)) #4
print(next(gen)) #5
print(next(gen)) #6
print(next(gen)) #7
print(next(gen)) #8
print(next(gen)) #9

print(next(gen)) #0
print(next(gen)) #1
print(next(gen)) #2
print(next(gen)) #3
print(next(gen)) #4
