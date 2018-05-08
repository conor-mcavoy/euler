import itertools
import operator

def prime(n):
    if n < 3: return n == 2
    if not n%2: return False
    for x in range(3, int(n**.5)+1, 2):
        if not n%x: return False
    return True

def next_prime(n):
    n += 1
    while not prime(n): n += 1
    return n

def prime_pair_set(size):
    start = 1
    primes = [next_prime(start)]
    primes.append(next_prime(primes[-1]))

    primes = [2, 3, 5]
    all_combos = set(itertools.combinations(primes, size))
    
    while True:
        for combo in all_combos:
            str_combo = map(str, combo)
            raw_pairs = itertools.permutations(str_combo, 2)
            all_pairs = map(lambda x: int(x[0]+x[1]), raw_pairs)
            
            if all(map(prime, all_pairs)):
                return combo
        primes.append(next_prime(primes[-1]))
        print(primes[-1])
        all_combos = set(itertools.combinations(primes, size)) - all_combos
    

print(prime_pair_set(3))
