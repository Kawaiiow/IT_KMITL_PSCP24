"""XI"""

def main():
    """void"""
    n = int(input())

    for i in range (1, n + 1):
        for j in range(0, n - i):
            print("  ", end=" ")
        for j in range(1, i + 1):
            print(f'{j:02}', end=" ")
        for j in range(i - 1, 0, -1):
            print(f'{j:02}', end=" ")
        print()
main()
