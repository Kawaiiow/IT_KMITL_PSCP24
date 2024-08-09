"""Harsh"""

def sumofuni(num):
    """int"""
    buffer = 0
    sign = 1
    if num < 0:
        sign *= -1
        num *= -1
    while num:
        buffer += num % 10
        num //= 10
    return buffer

def hasher(num):
    """void"""
    divider = sumofuni(num)

    if not num:
        print("No")
    elif not num % divider:
        print("Yes")
    elif num % divider:
        print("No")

def main():
    """void"""
    for _ in range(10):
        hasher(int(input()))
main()
