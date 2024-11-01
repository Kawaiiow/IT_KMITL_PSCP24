"""I"M SPEED! I SHOW SPEED!!!"""

import re

def main () -> None :
    """void"""
    target : int = int(input())
    n : int = int(input())
    speed = []
    start = []
    first = 0

    if not n:
        return
    for _ in range (n):
        msg = input().strip()
        msg = re.sub(r"[^0-9 ]", "", msg)
        speed.append(int(re.search(r"^\d+", msg).group()))
        start.append(int(re.search(r"\d+$", msg).group()))
    time = [ (target - start[i]) / speed[i] for i in range (n) ]
    for i in range (1,n):
        if time[i] < time[first] or \
            (time[i] == time[first] and speed[i] > speed[first]):
            first = i
    print(first + 1)
main()
