"""mod doc"""
def main():
    """doc"""
    y = int(input())
    x = int(input())
    sums = 0
    while x != -1:
        sums += x
        if sums == y:
            break
        x = int(input())
    print(sums)
main()
