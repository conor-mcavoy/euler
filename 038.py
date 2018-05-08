p = []

for multiplicand in range(1, 10000):
    for n in range(1, 10):
        multipliers = [x for x in range(1, n + 1)]
        all_prods = ''
        for each in multipliers:
            all_prods += str(each * multiplicand)
        if ''.join(sorted(all_prods)) == "123456789":
            p.append(all_prods)
            
q = [int(x) for x in p]
print(max(q))
