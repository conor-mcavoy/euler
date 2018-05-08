m = 0
for a in range(100):
    for b in range(100):
        s = 0
        for digit in str(a ** b):
            s += int(digit)
        if s > m:
            m = s
print(m)
