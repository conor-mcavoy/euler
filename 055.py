def isPalindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

def reverseAdd(num):
    return num + int(str(num)[::-1])

l = 0
for x in range(10000):
    num = x
    for counter in range(50):
        num = reverseAdd(num)
        if isPalindrome(num):
            break
    if counter == 49:
        l += 1
print(l)
