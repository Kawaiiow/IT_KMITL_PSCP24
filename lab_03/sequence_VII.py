"""VII"""

def main():
    """void"""
    n = int(input())

    for i in range(1, n + 1):
        for j in range (1, i + 1):
            print(j, end=" ")
        print()
    for i in range(0, n - 1):
        for j in range (1, n - i):
            print(j, end=" ")
        print()
main()
