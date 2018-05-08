from math import log

f = open("p099_base_exp.txt", "r")
a = []
for line in f:
    a.append((int(line[:line.index(",")]), int(line[line.index(",") + 1:-1])))
f.close()
a.pop()
a.append((13846, 725685))

print(714883 * log(15991, 511029))
##best_b = 2
##best_e = 2
##linenum = 0
##bestline = 0
##for pair in a:
##    linenum += 1
##    if best_e * log(best_b, pair[1]) < pair[0] and best_b > pair[1] or\
##       best_e * log(best_b, pair[1]) > pair[0] and best_b < pair[1]:
##        best_b, best_e = pair
##        bestline = linenum
##print(bestline, best_b, best_e)
