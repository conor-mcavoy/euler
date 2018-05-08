from math import ceil, sqrt

def is_prime(n):
    if not n % 2: return False
    for x in range(3, ceil(sqrt(n)) + 1, 2):
        if not n % x: return False
    return True

def all_rots_prime(num):
    string = str(num)
    for rot_num in range(len(string)):
        if not is_prime(int(string[rot_num:] + string[:rot_num])):
            return False
    return True



t = 4
for x in range(11, 1000000):
    if all_rots_prime(x):
        t += 1
print(t)
