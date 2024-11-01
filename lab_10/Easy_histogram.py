"""HISTORY REPEAT ITSELF"""

def main() -> None :
    """void"""
    msg : str = input().replace(" ", "")
    alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    res = {}

    for c in msg:
        if c in res:
            res.update({c: res.get(c) + 1})
        else:
            res.update({c: 1})
    for c in alpha:
        if c in res:
            print(f"{c} = {res.get(c)}")
main()
