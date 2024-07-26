"""arrow"""
K = int(input())
N = int(input())
for i in range(N):
    print(" "*((N//2)-(abs((N//2)-i))),end="")
    print("*"*K)
