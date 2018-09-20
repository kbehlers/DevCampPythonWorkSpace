"""
Program that prints the numbers from 1 to 100,
but for multiples of three print "Fizz" instead,
for multiples of five print "Buzz" instead, and
for multiples of both three and five print "FizzBuzz"
3 = "Fizz"
5 = "Buzz"
15 = "FizzBuzz"
"""
from math import sqrt as squareRoot
print(squareRoot(25))
def fizzbuzz(start=1, end=100):
    for num in range(start,end+1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()
