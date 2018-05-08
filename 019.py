totalSundays = 0
startDay = 2
for year in range(1901, 2001):
    for monthBump in [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]:
        if monthBump == 0 and year % 4 == 0:
            startDay += 1
        startDay += monthBump
        startDay %= 7
        if startDay == 0:
            totalSundays += 1

print(totalSundays)
