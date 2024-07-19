"""mod doc"""
def main():
    """doc"""
    x = int(input())
    n = 0
    if x < 0:
        x = - x
    if not x:
        n+=1
    while x>= 1000000000:
        x //= 1000000000
        n += 9
    while x>= 1000000:
        x //= 1000000
        n += 6
    while x>= 1000:
        x //= 1000
        n += 3
    while x:
        x //= 10
        n += 1
    print(n)
main()
