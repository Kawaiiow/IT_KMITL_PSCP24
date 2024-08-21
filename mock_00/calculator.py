"""Math"""

def main():
    """void"""
    n = int(input())
    t = 0

    if n > 1:
        for i in range(1, n + 1):
            t += len(str(i)) + 1
    else:
        t = 1
    print(t)
main()
