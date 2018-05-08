from itertools import permutations

t = 0
for number in permutations("0123456789"):
    s = ''.join(number)
    if not int(s[7:10]) % 17 and\
       not int(s[6:9]) % 13 and\
       not int(s[5:8]) % 11 and\
       not int(s[4:7]) % 7 and\
       not int(s[3:6]) % 5 and\
       not int(s[2:5]) % 3 and\
       not int(s[1:4]) % 2:
        t += int(s)
print(t)
