#problem 2
#3/19/15
a = 1
b = 2
n = 0
t = 2
while b < 4000000:
    a, b = b, a + b
    n += 1
    if not n % 3: t += b
print(t)
