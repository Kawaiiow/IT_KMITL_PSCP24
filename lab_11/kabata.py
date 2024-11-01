"""UGA??"""

import re

def main() -> None :
    """void"""
    n : int = int(input())
    res = []

    for _ in range (n):
        msg : str = input()
        if re.search(r"baka", msg):
            res.append("no")
            continue
        msg = msg.replace("bakka", "").replace("ba", "").replace("ta", \
                "").replace("ka", "")
        res.append("yes" if not msg else "no")
    print(*res, sep='\n')
main()
