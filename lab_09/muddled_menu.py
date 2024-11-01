"""Restaurant II, when??"""

import re

def main() -> None:
    """void"""
    msg : str = input()
    res = []

    while msg not in ("CLOSED", "DONE"):
        if msg == "SOMETHING'S WRONG":
            res.clear()
        elif re.search(r"Can't do: ", msg.strip()):
            res.remove(re.search(r"(?<=Can't do: ).+", msg).group().strip())
        elif re.search(r"#N$", msg.strip()):
            res.append(re.search(r"^[a-zA-Z0-9 ]+", msg).group().strip())
        elif re.search(r"#\d+$", msg.strip()):
            res.insert(int(re.search(r"\d+$", msg).group()) - 1, \
                       re.search(r"^[a-zA-Z0-9 ]+", msg).group().strip())
        msg : str = input()
    if msg == "CLOSED":
        res.clear()
    rev = list(reversed(res))
    print(f"Full Course: {res} Reversed: {rev}")
main()
