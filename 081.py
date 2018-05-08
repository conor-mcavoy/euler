f = open("p081_matrix.txt", "r")

d = []
for t in range(80):
    d.append(f.readline())
f.close()

square = []
for t in d:
    square.append([])
    temp = ""
    for x in t:
        if x == ",":
            square[-1].append(temp)
            temp = ""
        else:
            temp += x
    square[-1].append(temp[:-1])

diamond = []
for diag_len in range(1, 81):
    diamond.append([])
    for e in range(diag_len):
        diamond[-1].append(int(square[diag_len - e - 1][e]))
    

for diag_len in range(79, 0, -1):
    diamond.append([])
    for e in range(diag_len):
        diamond[-1].append(int(square[-e - 1][-diag_len + e]))

diamond.reverse()
for rn, row in enumerate(diamond[1:]):
    rn += 1
    for pos, element in enumerate(row):
        if rn < .5 * len(diamond):
            if pos != 0 and pos != len(row) - 1:
                diamond[rn][pos] += min(diamond[rn - 1][pos - 1],\
                                        diamond[rn - 1][pos])
            elif pos == 0:
                diamond[rn][pos] += diamond[rn - 1][0]
            else:
                diamond[rn][pos] += diamond[rn - 1][-1]
        else:
            diamond[rn][pos] += min(diamond[rn - 1][pos],\
                                    diamond[rn - 1][pos + 1])
print(diamond[-1][0])
