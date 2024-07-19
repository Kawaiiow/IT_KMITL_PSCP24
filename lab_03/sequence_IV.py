"""sequence"""

def main():
    """void"""
    n = int(input())
    count = 0
    for _ in range(n):
        for j in range(count + 1, count + n + 1):
            print(j, end=" ")
            count += 1
        print()
main()
