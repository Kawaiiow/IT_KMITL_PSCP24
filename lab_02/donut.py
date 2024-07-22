"""Blender Guru - Blender Tutorial for Complete Beginners \
    https://www.youtube.com/watch?v=B0J27sf9N1Y&list=PLjEaoINr3zgEPv5y--4MKpciLaoQYZB1Z """


def main():
    """void"""
    p = int(input())
    i = int(input())
    j = int(input())
    n = int(input())

    bundle = 0
    left = 0
    bundle = n // (i + j)
    left = n - (bundle * (i + j))
    if left >= i:
        left = 0
        bundle += 1
    print(((p * i) * bundle) + (p * left), ((i + j) * bundle) + (left))
main()
