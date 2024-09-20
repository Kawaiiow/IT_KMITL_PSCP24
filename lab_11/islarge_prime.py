"""IS prime?"""

def main():
    """void"""
    n = int(input())
    limit = n ** 0.5
    i = 2

    if n < 2:
        print("NO")
        return
    while i <= limit:
        if not n % i:
            print("NO")
            return
        i += 1
    print("YES")
main()
