"""OwO"""


def hamburger():
    """bruh"""
    a = int(input())
    b = int(input())
    c = (a + b) * 2
    r = ""

    while a:
        r += '|'
        a -= 1
    while c:
        r += '*'
        c -= 1
    while b:
        r += '|'
        b -= 1
    print(r)


hamburger()
