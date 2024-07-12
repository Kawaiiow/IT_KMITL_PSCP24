"""circle"""
import math

def main():
    """radius"""
    x = int(input())
    y = int(input())
    r = int(input())
    xn = int(input())
    yn = int(input())

    d = math.sqrt((xn - x)**2 + (yn - y)**2)
    if d > r:
        print("False")
    else:
        print("True")
main()
