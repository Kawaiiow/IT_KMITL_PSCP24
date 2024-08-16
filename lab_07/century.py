"""Universal Century"""
import re
import math

def main():
    """void"""
    n = int(input())
    century = 0

    for _ in range (n):
        msg = input()
        era = msg[:4]
        year = int(re.search(r"\d{1,4}", msg).group())
        if era == "B.E.":
            year -= 543
        century = math.ceil(year / 100)
        print(century)
main()
