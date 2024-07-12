"""RADAR CROSS SECTION"""
import math


def main():
    """void"""
    x = float(input())
    y = float(input())
    r = float(input())
    xn = float(input())
    yn = float(input())
    rn = float(input())

    if r + rn <= math.sqrt((xn - x)**2 + (yn - y)**2):
        print("No")
    else:
        print("Yes")
main()
