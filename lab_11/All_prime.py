"""Optimus Prime"""

def main():
    """void"""
    n = int(input())
    i = 2
    s = 1
    j = 0
    total = 0

    while i <= n:
        s = 1
        j = 2
        while j <= i // 2 and s:
            if not i % j:
                s = 0
            j += 1
        if s:
            total += 1
        i += 1
    print(total)
main()
