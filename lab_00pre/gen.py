import math, random


n = int(input("n : "));
r = int(input("max weight : "))
res = ""

for i in range(n * 2):
    res = res + str(math.floor(random.random() * r) + 1)
    if i != (n * 2) - 1:
        res = res + " "

# for i in range(n * 2):
#     res = res + str(math.floor(random.random() * r) + 1)
#     if i != (n * 2) - 1:
#         res = res + ", "

print(res)
