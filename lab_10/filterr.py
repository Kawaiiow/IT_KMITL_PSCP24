"""Air Filter"""
import json

def main() -> None :
    """void"""
    msg = input()
    n = float(input())
    dic: dict = json.loads(msg)
    valid = {key: val for (key, val) in dic.items() if val >= n}
    key = list(map(int, valid.keys()))
    key.sort()
    if valid:
        for k in key:
            print(f"{k}\t{dic[str(k)]:.2f}")
    else:
        print("Nope")
main()
