"Depress"

def main():
    """void"""
    p = int(float(input()) * 100)
    n = int(input())

    while n:
        p = p + (p * 381) // 10000
        n -= 1
    print(f"{p // 100}.{str(p)[-2:]:02}")
main()
