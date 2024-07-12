"""REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"""
import math


def main():
    """void"""
    x = float(input())
    y = float(input())
    r = float(input())
    xn = float(input())
    yn = float(input())

    d = math.sqrt((xn - x)**2 + (yn - y)**2)
    if d > r:
        print("No")
    else:
        print("Yes")
main()
