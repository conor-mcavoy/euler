with open('p079_keylog.txt') as f:
    triplets = set(f.read()[:-1].split('\n'))

#password = 10 ** (len(set(''.join(triplets))) - 1) - 1
password = 10236789

def check_pwd(pwd, trips):
    #print(pwd)
    for trip in trips:
#        if not set(trip) < set(pwd):
#            return False
        indices = [pwd.index(trip[0]), pwd.index(trip[1]), pwd.index(trip[2])]
        if indices != sorted(indices):
            return False
    return True

excluded_numbers = set('0123456789') - set(''.join(triplets))
included_numbers = set(''.join(triplets))

while not check_pwd(str(password), triplets):
    password += 1
    s = str(password)
    while included_numbers != set(s):
        if not excluded_numbers & set(s):
            password += 1
            s = str(password)
            continue
        for number in excluded_numbers & set(s):
            password += 10 ** (len(s) - s.index(number) - 1)
        s = str(password)

print(password)
print(sorted(triplets))
