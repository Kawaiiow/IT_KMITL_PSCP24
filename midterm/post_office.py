"""code"""

def box(w):
    """int"""
    p = 0

    if w > 1000:
        p = 70
    elif w > 500:
        p =55
    else:
        p = 45
    return p + 15

def sip(w):
    """int"""
    p = 0

    if w > 1000:
        p = 68
    elif w > 500:
        p = 48
    elif w > 250:
        p = 33
    elif w > 100:
        p = 28
    elif w > 20:
        p = 23
    elif w > 10:
        p = 18
    else:
        p = 16
    return p + 13

def main():
    """void"""
    n = int(input())
    m = int(input())
    total = 0

    for _ in range(n):
        total += sip(float(input()))
    for _ in range(m):
        total += box(float(input()))
    print(total)
main()
