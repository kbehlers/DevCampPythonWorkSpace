from die import Die
import pygal

#Create a D6
die = Die()

#Roll and store results
results = []
for roll_num in range(1000000):
    result = die.roll()
    results.append(result)

#Analyze results
frequencies = []

for value in range(1, die.num_sides+1):
    #Get the count of each face value
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [str(x) for x in range(1,7)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
