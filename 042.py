f = open("p042_words.txt", "r")
words = []
s = f.read()
f.close()
for pos, character in enumerate(s):
    if pos == len(s) - 1:
        break
    if character == '"' and s[pos + 1] != ",":
        nextp = s[pos + 1:].find('"')
        words.append(s[pos + 1:pos + nextp + 1])
def is_tri(n):
    x = 0
    while x * (x + 1) / 2 <= n:
        if x * (x + 1) / 2 == n:
            return True
        x += 1
    return False

t = 0
for word in words:
    s = sum([ord(x) - 64 for x in word])
    if is_tri(s):
        t += 1
print(t)
