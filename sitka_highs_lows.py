import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# get dates , and high and low temperatures from the file
    dates,highs, lows = [], [], []
    for row in reader:
        curr_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(curr_date)
        highs.append(high)
        lows.append(low)

# plot the high and low temperature
plt.style.use("seaborn")
fig,ax = plt.subplots()
ax.plot(dates,highs, c = "red", alpha = 0.5)
ax.plot(dates, lows, c = "blue", alpha = 0.5)
# we will use fill_method() to fill the space between two values
ax.fill_between(dates,highs,lows, facecolor = 'blue', alpha = 0.1)
# format plot
ax.set_title("Daily high and low temperatures - 2018", fontsize = 24)

plt.show()