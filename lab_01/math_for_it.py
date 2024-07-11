"""pi"""
import math

def main():
    """void"""
    r = float(input())
    area = math.pi*(r**2)
    Circumference = math.pi*r*2

    print(f'Area: {area:.3f}')
    print(f'Circumference: {Circumference:.3f}')
main()
