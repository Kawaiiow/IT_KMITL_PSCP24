"""Machine"""

def main():
    """void"""
    x = int(input())
    y = int(input())
    sums = 0

    print("pass : ", end="")
    if x <= y:
        for i in range(x, y + 1):
            if not i % 2 and i:
                sums += i
                print(f"{i} ", end="")
    else:
        while x >= y:
            if not x % 2 and x:
                sums += x
                print(f"{x} ", end="")
            x -= 1
    print(f"\nSum : {sums}")
main()
