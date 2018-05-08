from itertools import permutations

arrangements = permutations("0123456789")
b = 0
for arrangement in arrangements:
    n = [int(digit) for digit in ''.join(arrangement)]
    n[n.index(0)] = 10
    mag_num = sum(n[:3])
    if sum(n[2:5]) == mag_num and\
       sum(n[4:7]) == mag_num and\
       sum(n[6:9]) == mag_num and\
       n[8] + n[9] + n[1] == mag_num:
        c = [n[:3], [n[3], n[2], n[4]], [n[5], n[4], n[6]],\
             [n[7], n[6], n[8]], [n[9], n[8], n[1]]]
        lowest = 10
        for three in c:
            if three[0] < lowest:
                lowest = three[0]
                index = c.index(three)
        c = c[index:] + c[:index]
        s = ""
        for x in c:
            for y in x:
                s += str(y)
        if int(s) > b and len(s) == 16:
            b = int(s)
print(b)
        
