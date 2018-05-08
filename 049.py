from math import ceil, sqrt
from itertools import permutations as perm

def sieve(n):
    A = [True for x in range(n)]
    for i in range(2, ceil(sqrt(n)) + 1):
        if A[i]:
            for j in range(i ** 2, n, i):
                A[j] = False
    p = []
    for pos, x in enumerate(A):
        if x: p.append(pos)
    return p[2:]

p = sieve(10000)[168:]
new_p = []
for x in p:
    perms = set([''.join(c) for c in perm(str(x))])
    count = 0
    for permutation in perms:
        if int(permutation) in p:
            count += 1
        if count > 2:
            new_p.append(x)
            break
            

br = False
for prime in new_p:
    if prime == 1487:
        continue
    diff_max = ceil((10000 - prime) / 2)
    string = sorted(str(prime))
    for diff in range(2, diff_max + 1, 2):
        a = prime + diff
        b = a + diff
        if a not in new_p or b not in new_p or\
           sorted(str(a)) != string or\
           sorted(str(b)) != string:
            continue
        print(str(prime) + str(a) + str(b))
        br = True
    if br: break
        
