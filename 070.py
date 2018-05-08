def prime_divisors(n):
    p_divs = set()
    while not n%2:
        n //= 2
        p_divs.add(2)
    for x in range(3, int(n**.5)+1, 2):
        while not n%x:
            n //= x
            p_divs.add(x)
    if n != 1: return p_divs | {n}
    return p_divs

#def phi(n, p_divs):
    #p_divs = prime_divisors(n)
    



most = 0
for x in range(3, 10_000_000, 2):
    if not x%3 or not x%5 or not x%7 or not x%11 or not x%13 or not x%17: continue    
    p_divs = prime_divisors(x)
    if len(p_divs) != 2: continue
    numerator = 1
    denominator = 1
    for prime in p_divs:
        numerator *= prime - 1
        denominator *= prime
    tot = x * numerator // denominator
    
    if tot / x > most and sorted(str(x)) == sorted(str(tot)):
        best = x
        best_tot = tot
        most = tot / x
        print(best, best_tot, most, 1/most)
print(best, best_tot, most, 1/most)
