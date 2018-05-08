def sum_5th_powers(n):
    s = 0
    for dig in str(n):
        s += int(dig) ** 5
    return s
t = 0
for x in range(2, 999999):
    if x == sum_5th_powers(x): t += x
print(t)
