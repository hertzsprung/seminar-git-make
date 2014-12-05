#!/usr/bin/env python3
import sys
import datetime
import matplotlib.pyplot as plt

dates = []
rainfalls = []
for line in sys.stdin:
    tokens = line.strip().split(' ')
    date = datetime.datetime.strptime(tokens[0], '%Y-%m')
    rainfall = float(tokens[1])

    dates.append(date)
    rainfalls.append(rainfall)

plt.plot_date(dates, rainfalls, linestyle='-')
plt.savefig("heathrow-rain.pdf")
