"""arrow"""
K = int(input())
N = int(input())
for i in range(N):
    for j in range(abs((N//2)-i)):
        print(" ",end="")
    for j in range(K):
        print("*",end="")
        j = j*1
    print()
