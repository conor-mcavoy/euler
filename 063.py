b = 1
t = 0
while True:
    p = 1
    while len(str(b ** p)) == p:
        p += 1
        t += 1
    if p == 1: break
    b += 1
print(t)
