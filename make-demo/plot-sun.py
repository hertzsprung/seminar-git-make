#!/usr/bin/env python3
import sys
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

dates = []
sunshines = []
for line in sys.stdin:
    tokens = line.strip().split(' ')
    date = datetime.datetime.strptime(tokens[0], '%Y-%m')
    sunshine = float(tokens[1])

    dates.append(date)
    sunshines.append(sunshine)

plt.plot_date(dates, sunshines, linestyle='-')

xaxis = plt.gca().xaxis
xaxis.set_major_formatter(DateFormatter('%b'))

plt.savefig("heathrow-sun.pdf")
