"""MISSING LINK"""

def main() -> None :
    """void"""
    size : int = int(input())
    res = [1] * size
    n : int = int(input())

    while n:
        res[n - 1] = 0
        n : int = int(input())
    for i in range(size):
        if res[i]:
            print(i + 1)
main()
