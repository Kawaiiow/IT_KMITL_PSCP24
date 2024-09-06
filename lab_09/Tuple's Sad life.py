"""Tuple's Sad life"""
def main():
    """Tuple's Sad life"""
    x = tuple(input().split())
    y = input()
    count = x.count(y)
    index = x.index(y)
    for _ in range(count):
        for _ in range(count):
            print(f"{index}",end=" ")
        print()
main()
