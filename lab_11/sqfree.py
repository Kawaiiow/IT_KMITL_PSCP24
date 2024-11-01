"""Square??"""

def main() -> None :
    """void"""
    n : int = int(input())
    i = 1
    s = True
    j = 0
    total = 0

    while i <= n:
        s = True
        j = 2
        while j <= i ** 0.5 and s:
            if not i % j ** 2:
                s = False
            j += 1
        if s:
            total += 1
        i += 1
    print(total)
main()
