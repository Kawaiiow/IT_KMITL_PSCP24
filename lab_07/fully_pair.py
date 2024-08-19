"""Pair Programming is the best (Change my mind)."""
import re

def main():
    """void"""
    msg = input()
    res = ""

    for i in msg:
        buffer = msg.count(i)
        if buffer % 2:
            res += i
        msg = re.sub(i, "", msg)
    print(res if res else "fully paired")
main()
