import itertools

with open('p059_cipher.txt') as f:
    numbers = list(map(int, f.read().split(',')))

with open('1-1000.txt') as f:
    words = set(f.read().split('\n'))

# with open('ascii.txt') as f:
#     ascii

letters = 'abcdefghijklmnopgrstuvwxyz'
#possible_keys = [''.join(x) for x in permutations(letters, 3)]
possible_keys = set(itertools.product(list(letters), repeat=3))

best_score = 0
for key in possible_keys:
    decrypted_message = ''.join([chr(list(map(ord, key))[i % 3] ^ num) for i, num in enumerate(numbers)])

    score = 0
    for word in words:
        if word in decrypted_message:
            score += 1
    if score >= best_score:
        best_score = score
        best_message = decrypted_message

print(sum(map(ord, best_message)))