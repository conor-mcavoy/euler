from math import sqrt, floor

front = int(str(floor(sqrt(1929394959697989990)))[:-2])

while str(int(str(front) + "30") ** 2)[::2] != "1234567890" and\
      str(int(str(front) + "70") ** 2)[::2] != "1234567890":
    front -= 1
if str(int(str(front) + "30") ** 2)[::2] == "1234567890": print(str(front) + "30")
else: print(str(front) + "70")
