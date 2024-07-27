"""christmas"""

def leaf(n):
    """void"""
    for i in range(1, n + 1):
        print(" "*(n - i), end="")
        print("*"*i, end="")
        print("*"*(abs(i - 1)))

def tree(n, k):
    """void"""
    for _ in range(1,k + 1):
        print(" "*(n - 2), end="")
        print("-"*3)

def main():
    """void"""
    n = int(input())
    k = int(input())

    leaf(n)
    tree(n, k)
main()
