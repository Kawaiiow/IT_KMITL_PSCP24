"""Circle is just squaure with a lot of corner"""
import math

def main():
    """void"""
    r = float(input())
    a = float(input())
    b = float(input())

    circle = 2 * math.pi * r
    sq = (a + b) * 2
    if sq > circle:
        print("Rectangle is longer")
    elif circle > sq:
        print("Circle is longer")
    else:
        print("Equal")
    print(f"{abs(circle - sq):.5f}")
main()
