"""Uni"""

def decoder(num):
    """void"""
    while num >= 10:
        buffer = 0
        while num:
            buffer += num % 10
            num //= 10
        num = buffer
    print(num)

def main():
    """void"""
    msg = int(input())
    while msg:
        decoder(msg)
        msg = int(input())
main()
