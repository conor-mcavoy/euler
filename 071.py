e = 1

for d in range(2, 1000001):
    n = int(3.0 * d / 7.0) - 1.0
    while n / d < 3.0 / 7.0: n += 1.0
    if 3.0 / 7.0 - (n - 1) / d < e:
        e = 3.0 / 7.0 - (n - 1) / d
        m = n - 1
print(int(m))
