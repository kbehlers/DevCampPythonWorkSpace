from functools import reduce
import time
from decimal import Decimal



def manual_exponent(base, exponent):
    counter = 1
    multiplier = base
    while counter < exponent:
        base *= multiplier
        counter += 1
    return base


def manual_exponent_functional(num, exp):
    computed_list = [num] * exp
    return (reduce(lambda total, element: total * element, computed_list))


startLoop = time.clock()
manual_exponent(10,3)
endLoop = time.clock()

startFunctional = time.clock()
manual_exponent_functional(10,3)
endFunctional = time.clock()

print(Decimal(endLoop-startLoop))
print(Decimal(endFunctional-startFunctional))
