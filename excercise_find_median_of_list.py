#in real life, use a stats library

import math

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_sale_prices = sorted(sale_prices)
sorted_sale_prices_length = len(sorted_sale_prices)
index_of_median = math.floor(sorted_sale_prices_length/2)
median = sorted_sale_prices[index_of_median]
print(median)