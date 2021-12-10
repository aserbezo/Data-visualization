import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #for index_column_header in enumerate(header_row):
       # print(index_column_header)
        # Here we see that the dates and their high temperatures are stored in columns 2 and 5. To explore this data,
        # we’ll process each row of data in sitka_weather_07-2018_simple.csv and extract the values with the indexes 2
        # and 5.

    # get the high temperature and dates from the file
    dates,highs = [], []
    for row in reader:
        curr_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(curr_date)
        highs.append(high)

# plot the high temperatures
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates,highs, c = "red")

# format plot
ax.set_title("Daily high temperatures - 2018", fontsize = 24)
ax.set_xlabel("", fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)",fontsize = 24)
ax.tick_params(axis = "both",which = "major", labelsize = 16)

plt.show()
