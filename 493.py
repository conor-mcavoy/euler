import random
#import itertools

def unique_balls(picks, balls, iters=10000):
    all_balls = "ROYGBIV"*balls
    unique = 0
    for _ in range(iters):
        unique += len(set(random.sample(all_balls, picks)))
    return unique/iters

print(unique_balls(2, 2, 100000))
