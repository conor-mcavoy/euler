total = 11

for x in range(1, 1000):
    last = total
    
    ones = x % 10
    if   ones == 1 or ones == 2 or ones == 6:
        total += 3
    elif ones == 3 or ones == 7 or ones == 8:
        total += 5
    elif ones == 4 or ones == 5 or ones == 9:
        total += 4

    tens = int(x % 100 - ones)
    if   tens == 20 or tens == 30 or tens == 80 or tens == 90:
        total += 6
    elif tens == 40 or tens == 50 or tens == 60:
        total += 5
    elif tens == 70:
        total += 7
    elif tens == 10:
        if   ones == 1 or ones == 2 or ones == 3 or\
             ones == 5 or ones == 0 or ones == 8:
            total += 3
        elif ones == 4 or ones == 6 or ones == 7 or ones == 9:
            total += 4
    
    hundreds = x - tens - ones
    if hundreds > 0 and (tens != 0 or ones != 0):
        total += 3
    if hundreds > 0:
        total += 7
        if   hundreds == 100 or hundreds == 200 or hundreds == 600:
            total += 3
        elif hundreds == 300 or hundreds == 700 or hundreds == 800:
            total += 5
        elif hundreds == 400 or hundreds == 500 or hundreds == 900:
            total += 4
    
print(total)
