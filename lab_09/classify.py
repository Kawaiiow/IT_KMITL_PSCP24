"""Average WT player with document"""

def main() -> None:
    """void"""
    id_list = []
    buffer = 0
    count = 1
    msg: str = input()

    while msg != "END":
        msg = int(msg)
        id_list.append(msg // 10000)
        msg = input()
    id_list.sort()
    year = ""
    idx = ""
    for m in id_list:
        if not buffer:
            buffer = m
            year, idx = (str(buffer // 100), str(buffer % 100))
        elif buffer == m:
            count += 1
        elif buffer // 100 == m // 100 and buffer % 100 != m % 100:
            print(year, idx, count)
            buffer = m
            year, idx = ("--", str(buffer % 100))
            count = 1
        else:
            print(year, idx, count)
            buffer = m
            year, idx = (str(buffer // 100), str(buffer % 100))
            count = 1
    print(year, idx, count)
main()
