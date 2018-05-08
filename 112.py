"""Working from left-to-right if no digit is exceeded by the digit to its left
it is called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a
"bouncy" number; for example, 155349.
Clearly there cannot be any bouncy numbers below one-hundred, but just over
half of the numbers below one-thousand (525) are bouncy. In fact, the least
number for which the proportion of bouncy numbers first reaches 50% is 538.
Surprisingly, bouncy numbers become more and more common and by the time we
reach 21780 the proportion of bouncy numbers is equal to 90%.
Find the least number for which the proportion of bouncy numbers is exactly
99%."""

def bouncy(n):
    """Determines if the number is bouncy."""
    down = False
    up = False
    for pos, digit in enumerate(str(n)[:-1]):
        if int(digit) - int(str(n)[pos + 1]) > 0: up = True
        if int(digit) - int(str(n)[pos + 1]) < 0: down = True
        if up and down: return True
    return False

t = 0
x = 0
while True:
    if bouncy(x): t += 1
    if x != 0 and 100 * t == 99 * x:
        print(x)
        break
    x += 1

#Prints 1587000
#Completed 2016-07-16
