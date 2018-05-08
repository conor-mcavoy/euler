from math import ceil, sqrt

def is_comp(n):
    if not n % 2 or not n % 3: return True
    for x in range(6, ceil(sqrt(n)) + 1, 6):
        if not n % (x - 1) or not n % (x + 1): return True
    return False
    
t = 1
while True:
    t += 2
    s = str(t)
    if s.count("1") == 3 and s[-1] != "1":
        if s[0] == "1":
            start = 1
        else:
            start = 0
        count = 0
        for digit in range(start, 10):
            if is_comp(int(s.replace("1", str(digit)))):
                count += 1
            if count > 2 - start:
                break
        if count == 2 - start:
            print(s)
            break
