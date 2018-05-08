def pascalsTri(n):
    """Row 1 is considered 1 1, row 2 is 1 2 1"""
    triangle = [[1, 1]]

    for currentRow in range(2, n + 1):
        lastRow = triangle[len(triangle) - 1]
        nextRow = [0]
        for number in lastRow:
            nextRow[len(nextRow) - 1] += number
            nextRow.append(number)
        triangle.append(nextRow)
    return triangle

sums = 0
for x in pascalsTri(20)[19]:
    sums += x ** 2
print(sums)
