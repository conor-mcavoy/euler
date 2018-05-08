f = open("p067_triangle.txt")
triangle = []
temp = []
num = []
while True:
    c = f.read(1)
    if c != "\n" and c != " ":
        num.append(c)
    elif c == " ":
        temp.append(int(''.join(num)))
        num = []
    else:
        temp.append(int(''.join(num)))
        num = []
        triangle.append(temp)
        temp = []
    if not c:
        break
f.close()

triangle.reverse()
for rowNum, currentRow in enumerate(triangle[:-1]):
    for index, number in enumerate(currentRow[:-1]):
        triangle[rowNum + 1][index] += max(number, currentRow[index + 1])

print(triangle[-1][0])
