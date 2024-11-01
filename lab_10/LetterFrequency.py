"""SO LONG!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""

import re

def main() -> None :
    """void"""
    msg : str = re.sub(r"[^a-zA-Z]", "",input()).lower()
    res = {}

    for c in msg:
        if c in res:
            res.update({c: res.get(c) + 1})
        else:
            res.update({c: 1})
    print(max(res, key=res.get))
main()
