def nekst(p, q):
    return (2 * q + p, q + p)

n = 3
d = 2
t = 0
for x in range(1000):
    n, d = nekst(n, d)
    if len(str(n)) > len(str(d)):
        t += 1
print(t)
