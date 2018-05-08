#problem 6
#3/19/15

sumsq = 0
sqsum = 0
for x in range(101):
    sumsq += x ** 2
    sqsum += x
print(sqsum ** 2 - sumsq)
