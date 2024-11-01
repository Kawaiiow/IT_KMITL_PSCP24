"""War never change"""
import json

def main() -> None :
    """void"""
    atk_unit : list = sorted(json.loads(input()), reverse = True)
    fed_unit : list = sorted(json.loads(input()), reverse = True)
    total : int = 0
    i : int = 0
    j : int = 0

    while i < len(fed_unit):
        while atk_unit[j] <= fed_unit[i] and i < len(fed_unit) - 1:
            i += 1
        total += atk_unit[j] if atk_unit[j] > fed_unit[i] else 0
        j += 1
        i += 1
    print(total)
main()
