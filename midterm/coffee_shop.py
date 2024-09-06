"""coffee"""

def main():
    """cafe"""
    p = float(input())
    b_per = float(input())
    c_per = float(input())
    exrate = float(input())
    target = int(input())
    firstform = (p) + (((target - 1) * p) * (1 - (b_per / 100))) if target > 1 else p
    sec_form = (p * target) * (1 - (c_per / 100)) if p * target >= exrate else p * target

    print("1" if firstform < sec_form else "2")
    print(f"{firstform:.2f}" if firstform < sec_form else f"{sec_form:.2f}")
main()
