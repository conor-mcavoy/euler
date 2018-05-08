def divisors(n):
    divs = {n}
    for x in range(2, int(n**.5)+1):
        if not n%x: divs.update({x, n//x})
    return divs

def fac_divisors(n, previous, below):
    if n == 1: return {1}
    output = set()
    for div in divisors(n):
        output.update({div*x for x in previous if div*x <= below and div*x not in previous})
    return output

all_divisors = set()
n = 10000
total = -1
for x in range(1, n+1):
    #new_divisors = fac_divisors(x, {*all_divisors.keys()}, n) - {*all_divisors.keys()}
    new_divisors = fac_divisors(x, all_divisors, n) #- all_divisors
    all_divisors.update(new_divisors)
    total += x*len(new_divisors)
    #print(x, new_divisors)
    #for div in new_divisors:
        #all_divisors.add(div)
        #total += x
print(total)


