import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row =next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)


    dates,highs, lows = [], [], []
    for row in reader:
        curr_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {curr_date}")
        else:
            dates.append(curr_date)
            highs.append(high)
            lows.append(low)

plt.style.use("seaborn")
fig,ax = plt.subplots()
ax.plot(dates,highs, c = "red", alpha = 0.5)
ax.plot(dates, lows, c = "blue", alpha = 0.5)
# we will use fill_method() to fill the space between two values
ax.fill_between(dates,highs,lows, facecolor = 'blue', alpha = 0.1)
# format plot
title = "Daily high and low temperatures - 2018\n Death Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel("", fontsize = 16)

plt.show()