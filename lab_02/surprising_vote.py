"""WOWWWWWWWWWWWW!!!!!!"""


def main():
    """void"""
    sums = float(input())
    top = float(input())
    two = 0
    p1 = 0
    p2 = 0
    if top > sums or top * 2 < sums - top or top < 0 or sums < 0:
        return
    two = sums - top
    p1 = two / 2
    p2 = two - p1
    while p1 <= top and p2 >= 0:
        if abs(top - p1) > 2 or abs(top - p2) > 2:
            print("Surprising")
            return
        p1 += 0.1
        p2 -= 0.1
    print("Not surprising")
main()
