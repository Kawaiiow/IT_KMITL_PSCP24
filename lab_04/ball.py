"""ball"""
X = float(input())
Y = 0
X *= 3/5
while X >= 0.01:
    Y += 1
    X *= 3/5
print(Y)
