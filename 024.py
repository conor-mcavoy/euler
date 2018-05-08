import itertools

x = [a for a in itertools.permutations("0123456789", 10)]
print(''.join(x[999999]))
