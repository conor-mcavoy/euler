from math import log, ceil

m = 0
dmax = 0
for d in range(3, 1000, 2):
    if not d % 5:
        continue
    n = 9
    while n % d:
        n = int("9" + str(n))
    if len(str(n)) > m:
        m = len(str(n))
        dmax = d
print(dmax)
