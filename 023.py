import math

def sumOfDivs(n):
    t = 0
    for x in range(1, math.ceil(math.sqrt(n))):
        if n % x == 0:
            t += x + int(n/x)
    if math.sqrt(n) == int(math.sqrt(n)):
        t += int(math.sqrt(n))
    return t - n

allAbuns = []
for x in range(28123):
    if x < sumOfDivs(x):
        allAbuns.append(x)

allAddts = []
for pos, x in enumerate(allAbuns):
    for y in allAbuns[pos:]:
        if x + y < 28123: allAddts.append(x + y)

allAddts = list(set(allAddts))
print(int(28123 * 28122 / 2 - sum(allAddts)))



