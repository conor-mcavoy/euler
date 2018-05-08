"""Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d <= 8 in ascending order of
size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that there are 21 elements in this set.
How many elements would be contained in the set of reduced proper fractions for
d <= 1,000,000?"""

def prime_factors(n):
    pfs = set()
    while not n % 2:
        pfs.add(2)
        n /= 2
    for x in range(3, int((1.0 * n) ** .5) + 1, 2):
        while not n % x:
            pfs.add(x)
            n /= x
    if n != 1: pfs.add(n)
    return pfs

def totient(num):
    n = num
    d = 1
    for x in prime_factors(num):
        n *= x - 1
        d *= x
    return n / d

def farey(n):
    return sum([totient(x) for x in range(1, n + 1)]) - 1

print(farey(1000000))

#Prints 303963552391
#Completed 2016-02-05
