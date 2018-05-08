from itertools import permutations

def pan(a, b, c):
    d = ''.join(sorted(a + b + str(c)))
    if d == '123456789': return True
    return False

def splits_pan(string):
    length = len(string)
    for split_pt in range(1, length):
        if pan(string[:split_pt], string[split_pt:], int(string[:split_pt]) *\
               int(string[split_pt:])):
            return int(string[:split_pt]) * int(string[split_pt:])
    return False

products = []
for l in range(2, 6):
    for x in permutations('123456789', l):
        x = ''.join(x)
        if splits_pan(x):
            products.append(splits_pan(x))
print(sum(set(products)))

