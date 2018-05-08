#problem 4
#3/19/15
def pal(n):
    s = str(n)
    if s[::-1] == s:
        return True
    return False

best = 0
for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        if x * y > best and pal(x * y):
            best = x * y
print(best)
          
