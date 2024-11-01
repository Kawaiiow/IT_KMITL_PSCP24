"""MISSING LINK"""

def main() -> None :
    """void"""
    size : int = int(input())
    res = set(range(1, size + 1))
    cmp = set()
    n : int = int(input())

    while n:
        cmp.add(n)
        n : int = int(input())
    if res - cmp:
        print(*sorted(res - cmp), sep='\n')
    else:
        print("Nope")
main()
