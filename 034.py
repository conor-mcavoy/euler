from math import factorial as fac

s = '9'
while int(s) < fac(9) * len(s):
    s += '9'
t = 0
for x in range(10, int(s)):
    if x == sum([fac(int(a)) for a in str(x)]):
        t += x
print(t)
    
