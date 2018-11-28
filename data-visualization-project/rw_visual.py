import matplotlib.pyplot as plt

#My modules
from random_walk import RandomWalk

#Make a random walk and plot points
rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()