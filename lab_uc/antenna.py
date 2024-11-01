"""Wireless"""
import json

def main() -> None :
    """void"""
    r : int = int(input())
    pos : list = list(map(int, json.loads(input())))
    pos.sort()
    green = 0
    n = 0

    for p in pos:
        if not green:
            green = p + r * 2
            n += 1
        elif p > green:
            green = p + r * 2
            n += 1
    print(n)
main()
