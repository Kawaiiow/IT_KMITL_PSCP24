"""RTFM"""

def wormread() -> None :
    """void"""
    limit : float = float(input())
    n : int = int(input())
    time_lists = [float(input()) for _ in range (n)]
    time_lists.sort()
    i : int = 0
    total : float = 0

    while i < n and total + time_lists[i] <= limit:
        total += time_lists[i]
        i += 1
    print(i)

def main() -> None :
    """void"""
    n : int = int(input())

    for _ in range (n):
        wormread()
main()
