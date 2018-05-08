from math import factorial as fac
#from itertools import combinations as comb

def p(s, n):
    return int((n ** 2 * (s - 2) - n * (s - 4)) / 2)

def is_fig(num, fig):
    n = 1
    while p(fig, n) < num:
        n += 1
    if p(fig, n) == num:
        return True
    return False

cyclics = []
for x in range(1000, 10000):
    for fig in range(3, 9):
        if is_fig(x, fig) and str(x // 10)[-1] != "0":
            cyclics.append(x)
            break
print(cyclics)
print(len(cyclics))

def create_chains(x, chains):
    

for cyc in cyclics:
    create_chains(cyc, None)

