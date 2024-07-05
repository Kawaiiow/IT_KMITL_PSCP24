"""sign"""


import math


def sign():
    """TURN U IDIOT"""
    k = int(input())
    n = int(input())

    i = 0
    while i < n:
        res = ""
        j = 0
        m = 0
        while j < math.sqrt(((n // 2) - i) ** 2):
            res += " "
            j += 1
        while m < k:
            res += "*"
            m += 1
        print(res)
        i += 1


sign()
