cache = {0: 2, 1: 1, 2: 1, 145: 1, 169: 3, 871: 2, 872: 2, 1454: 3, 45361: 2,\
         40585: 1, 45362: 2, 363601: 3}

f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

t = 0
for x in range(1000000):
    temp = x
    c = 0
    while temp not in cache:
        c += 1
        temp = sum([f[int(d)] for d in str(temp)])
    c += cache[temp]
    cache[x] = c
    if c == 60: t += 1
print(t)
