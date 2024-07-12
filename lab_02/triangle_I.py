"""triangle"""


def n_cmp(n1, n2):
    """cmp"""
    if n1 > n2:
        return 1
    return 0


def main():
    """45"""
    a = float(input())
    b = float(input())
    c = float(input())

    if n_cmp(a, b):
        a = a + b
        b = a - b
        a = a - b
    if n_cmp(b, c):
        b = c + b
        c = b - c
        b = b - c
    if n_cmp(a, b):
        a = a + b
        b = a - b
        a = a - b

    if a <= 0 or b <= 0 or c <= 0:
        print("No")
    elif 0 <= abs(c**2 - (a**2 + b**2)) <= 0.01:
        print("Yes")
    else:
        print("No")
main()
