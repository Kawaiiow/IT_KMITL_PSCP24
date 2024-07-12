"""Bob"""

def main():
    """void"""
    m = int(input())
    n = int(input())
    r = int(input())
    use_n = 0

    if m < 0:
        m = 0
    if n < 0:
        n = 0

    use_n = r // 5
    if use_n > n:
        use_n = n
    r -= 5 * use_n
    if m >= r:
        print(r)
    else:
        print("-1")
main()
