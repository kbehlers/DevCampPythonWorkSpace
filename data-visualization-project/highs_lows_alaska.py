import csv
from datetime import datetime
from matplotlib import pyplot as plt


#Read dates, highs, and lows temperatures from file
# filename = 'data-visualization-project\sitka_weather_07-2014.csv'
filename = 'C:/Users/Copy/Documents/DevCampPythonWorkSpace/data-visualization-project/sitka_weather_2014.csv'
with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)


#Plot temperatures
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='purple', alpha=0.1)

#Format plot
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.ylim(-50, 150) 
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()