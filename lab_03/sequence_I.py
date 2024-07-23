"""I"""

def main():
    """void"""
    n = int(input())

    for _ in range(n):
        for i in range(1, n + 1):
            print(i, end=" ")
        print()
main()
