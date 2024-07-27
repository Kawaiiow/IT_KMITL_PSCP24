"""bill"""
X = int(input())
Y = X*0.1
if Y < 50:
    Y = 50
elif Y > 1000:
    Y = 1000
Z = X + Y
Z = Z*1.07
print(f"{Z:.2f}")
