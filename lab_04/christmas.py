"""christmas"""

def leaf(n):
    """void"""
    for i in range(1, n + 1):
        print(" "*(n - i), end="")
        print("*"*i, end="")
        print("*"*(abs(i - 1)))

def tree(k, n):
    """void"""
    for i in range(1,n + 1):
        print(" "*(k - 3), end=" ")
        print("-"*3)

def main():
    """void"""
    n = int(input())
    k = int(input())

    leaf(n)
    tree(n, k)
main()
