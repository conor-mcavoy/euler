#problem 1
#3/19/15
t = 0
for x in range(1000):
    if not x % 3 or not x % 5: t += x
print(t)
