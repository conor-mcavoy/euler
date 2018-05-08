t = 0
for number in range(1, 1000000, 2):
    if str(number) == str(number)[::-1] and\
       str(bin(number)[2:]) == str(bin(number)[2:])[::-1]:
        t += number
print(t)
