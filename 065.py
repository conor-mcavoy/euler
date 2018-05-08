fracs = []

for x in range(99):
    if (x - 1) % 3 == 0:
        fracs.append(2 * (x + 2) // 3) 
    else:
        fracs.append(1)


n = fracs[-1]
d = 1
for a in fracs[-2::-1]:
    n, d = d + n * a, n

t = 0
for dig in str(d + 2 * n):
    t += int(dig)
print(t)
