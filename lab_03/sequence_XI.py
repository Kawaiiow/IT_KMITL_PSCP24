"""XI"""

def main():
    """void"""
    n = int(input())

    for i in range(-n + 1, n, 1):
        for j in range(-n + 1, n, 1):
            if abs(i) > abs(j) - 1:
                print(f"{n - abs(i):02}", end=" ")
            else:
                print(f"{n - abs(j):02}", end=" ")
        print()
main()
