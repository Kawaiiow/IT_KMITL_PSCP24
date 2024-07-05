"""doc"""
import math

def main():
    """void"""
    x = int(input())
    y = int(input())
    z = int(input())

    print(x+1)
    print(7*(y**3)+2*(y**2)-31*y+1)
    print(-z)
    print((x+y)*(x-y))
    print((y - math.sqrt(y**2 - (4*x*z)))/(2*x))
main()
