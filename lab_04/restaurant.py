"""Yum Yum"""

def main():
    """void"""
    current = float(input())
    trig = float(input())
    percent = float(input())
    add = float(input())
    sums = current + add
    discount = 0

    if sums >= trig:
        discount = sums * (percent/100)
        if discount == add:
            print("Yes")
        elif discount > add:
            print(f"Yes {abs(sums - (sums - discount)):.3f}")
        elif discount < add:
            print(f"No {abs(sums - (sums - discount)):.3f}")
    else:
        print("Yes")
main()
