# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Caleb Mandapat
# Section:      509
# Assignment:   12.15
# Date:         19 November 2023
#
import numpy as np
import matplotlib.pyplot as plt

fname = "WeatherDataCLL.csv"

#  plot 1

maxTemps = []
avgWindSpd = []

with open(fname, "r") as f:
    lines = f.read().split("\n")
    for i in lines[1:]:
        i = i.split(",")
        if i[-2] == '':
            continue
        else:
            maxTemps.append(int(i[-2]))
    for j in lines[1:]:
        j = j.split(",")
        if j[1] == '':
            continue
        else:
            avgWindSpd.append(float(j[1]))
# print(avgWindSpd)
arrTemps = np.array(maxTemps)
arrWind = np.array(avgWindSpd)
xs = [x for x in range(len(arrTemps))]
fig, ax1 = plt.subplots()
ax1.set_xlabel('Dates')
ax1.set_ylabel('Maximum Temperature')
lns1 = ax1.plot(xs, arrTemps[0:], c='r', label='Max Temp')

ax2 = ax1.twinx()
xs = [x for x in range(len(arrWind))]
ax2.set_ylabel('Average Wind Speed')
lns2 = ax2.plot(xs, arrWind[0:], c='b', label='Avg Wind')

lns = lns1 + lns2
labs = [l.get_label() for l in lns]
plt.legend(lns, labs, loc='lower left')
plt.show()

#  plot 2

plt.hist(avgWindSpd, color='g', edgecolor='k', bins=29)
plt.title('Histogram of Average Wind Speed')
plt.xlabel('Number of days')
plt.ylabel('Average Wind Speed (mph)')
plt.show()

#  plot 3
precip = []
avgHumid = []
with open(fname, 'r') as f:
    lines = f.read().split("\n")
    for i in lines[1:]:
        i = i.split(',')
        if i[2] != '' and i[3] != '':
            precip.append(float(i[2]))
            avgHumid.append(int(i[3]))
plt.scatter(avgHumid, precip, s=5, c='k')
plt.title('Precipitation vs Average Relative Humidity')
plt.xlabel('Average Relative Humidity (%)')
plt.ylabel('Precipitation (in)')
plt.show()

#  plot 4
#  dictionaries
avgTemps = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': [],
            '12': []}
monthMaxs = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}
monthMins = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}

with open(fname, 'r') as f:
    lines = f.read().split("\n")
    for i in lines[1:]:
        i = i.split(',')
        if i[4] != '':
            avgTemps[i[0].split('/')[0]].append(int(i[4]))
        if i[-2] != '':
            monthMaxs[int(i[0].split('/')[0])].append(int(i[-2]))
        if i[-1] != '' and i[-1] != '\n':
            monthMins[int(i[0].split('/')[0])].append(int(i[-1]))

months = list(avgTemps.keys())
avgs = []
maxs = []
mins = []

for value in avgTemps.values():
    value = sum(value) / len(value)
    avgs.append(value)
for value in monthMaxs.values():
    value = max(value)
    maxs.append(value)
for value in monthMins.values():
    value = min(value)
    mins.append(value)

plt.bar(months, avgs, color='y')
plt.plot(months, maxs, color='r', label='High T')
plt.plot(months, mins, color='b', label='Low T')
plt.title('Temperature by Month')
plt.xlabel('Month')
plt.ylabel('Average Temperature (F)')
plt.legend(loc='upper right')
plt.show()
