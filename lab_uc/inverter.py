"""Invert this"""

def main() -> None :
    """void"""
    msg = input()
    res = ""

    for c in msg:
        if c == '1':
            res += '0'
        else:
            res += '1'
    print(res.lstrip("0"))
main()
