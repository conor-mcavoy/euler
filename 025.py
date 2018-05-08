from math import log

a = 1
b = 1
c = 1
while log(a, 10) < 999:
    c += 1
    a, b = b, a+b
print(c)
