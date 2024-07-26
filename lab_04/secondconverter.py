"""Converter"""

def main():
    """void"""
    k = int(input())
    s = int(input())
    m = int(input())
    h = int(input())

    sec = k % s
    mins = k // s
    hour = mins // m
    hour %= h
    mins %= m
    print(f"{hour}:{mins}:{sec}")
main()
