def intersection(a, b):
    if str(a)[0] in str(b): return str(a)[0]
    else: return str(a)[1]

array = []
for a in range(10, 100):
    for b in range(10, 100):
        if str(b)[0] not in str(a) and str(b)[1] not in str(a):
            continue
        if not a % 10 and not b % 10:
            continue
        if a >= b:
            continue
        inter = intersection(a, b)
        c = str(a).replace(inter, "")
        if c == "":
            c = inter
        d = str(b).replace(inter, "")
        if d == "":
            d = inter
        c = int(c)
        d = int(d)
        if not a or not b or not c or not d:
            continue
        if a / b == c / d:
            array.append((a, b))
tnum = 1
tdenom = 1
for frac in array:
    num, denom = frac
    tnum *= num
    tdenom *= denom
final = tnum / tdenom
for x in range(2, tdenom):
    if final * x == int(final * x):
        print(x)
        break
