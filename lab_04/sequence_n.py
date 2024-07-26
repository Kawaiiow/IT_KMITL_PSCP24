"""sequence N"""

def main():
    """void"""
    n = int(input())

    for i in range(n):
        print("*", end="")
        for j in range(n - 1):
            if j and j != n - 1 and j == i:
                print("*", end="")
            elif j and j != n - 1:
                print(" ", end="")
        print("*", end="")
        print()
main()
