"""Diff"""

def main():
    """void"""
    a = int(input())
    b = int(input())
    set_a = {input() for _ in range (a)}
    set_b = {input() for _ in range (b)}
    diff = set_a - set_b
    msg = ""
    res = ""

    for c in diff:
        msg += c + ' '
    msg = sorted(map(int, msg.split()))
    for c in msg:
        res += str(c) + ' '
    print(res)
main()
