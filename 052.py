t = 0
while True:
    t += 1
    digits = sorted(str(t))
    result = True
    for m in range(2, 7):
        if digits != sorted(str(m * t)):
            result = False
            break
    if result:
        print(t)
        break
        
