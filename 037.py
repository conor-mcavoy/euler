from math import ceil, sqrt

def is_prime(n):
    if n == 1 or n == 0: return False
    if n == 2: return True
    if not n % 2: return False
    for x in range(3, ceil(sqrt(n)) + 1, 2):
        if not n % x: return False
    return True

def trunc(number):
    string = str(number)
    for trunc_pt in range(len(string)):
        if not is_prime(int(string[trunc_pt:])) or\
           not is_prime(int(string[:trunc_pt + 1])):
            return False
    return True

t = 0
s = 0
c = 11
while t < 11:
    if trunc(c):
        t += 1
        s += c
    c += 1
print(s)
