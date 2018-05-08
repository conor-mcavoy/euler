from itertools import permutations

x = 1000
counter = 331
counter2 = 66
cubes = {}
current_length = 4
lowest = {}
while True:
    x += counter
    counter += counter2
    counter2 += 6
    s = ''.join(sorted(str(x)))
    if len(str(x)) > current_length:
        cubes = {}
        current_length += 1
    if s in cubes:
        cubes[s] += 1
    else:
        cubes[s] = 1
        lowest[s] = x
    if cubes[s] == 5:
        print(lowest[s])
        break
