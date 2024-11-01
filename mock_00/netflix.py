"""NETFLIX"""

PRM = (1, 419, -4)
STD = (1, 349, -2)
BSC = (1, 279, -1)
MOB = (1, 99, -1)

def get_req() -> None :
    """int"""
    req_code = ""

    for _ in range(5):
        c = input()
        if c == "Yes":
            req_code += '1'
        else:
            req_code += '0'
    return req_code.rfind('1') + 1

def main() -> None :
    """void"""
    n : int = max(int(input()), int(input()))
    req_code = get_req()
    total, mob, bsc, std, prm = (0, 0, 0, 0, 0)

    while n > 0:
        if req_code == 5:
            prm, total, n = tuple(map(lambda i, j: i + j, (prm, total, n), PRM))
        elif req_code == 4 and n >= 3:
            prm, total, n = tuple(map(lambda i, j: i + j, (prm, total, n), PRM))
        elif req_code == 4 and n < 3:
            std, total, n = tuple(map(lambda i, j: i + j, (std, total, n), STD))
        elif req_code == 3 and n >= 3:
            prm, total, n = tuple(map(lambda i, j: i + j, (prm, total, n), PRM))
        elif req_code == 3 and n >= 2:
            std, total, n = tuple(map(lambda i, j: i + j, (std, total, n), STD))
        elif req_code == 3:
            bsc, total, n = tuple(map(lambda i, j: i + j, (bsc, total, n), BSC))
        elif req_code <= 2:
            mob, total, n = tuple(map(lambda i, j: i + j, (mob, total, n), MOB))
    print(f"Premium x {prm}\n" if prm else "", end="")
    print(f"Standard x {std}\n" if std else "", end="")
    print(f"Basic x {bsc}\n" if bsc else "", end="")
    print(f"Mobile x {mob}\n" if mob else "", end="")
    print(f"Total = {total} THB")
main()
