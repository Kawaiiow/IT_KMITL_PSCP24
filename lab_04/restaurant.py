"""Yum Yum"""

def main():
    """void"""
    current = float(input())
    trig = float(input())
    percent = float(input())
    add = float(input())
    sums = current + add
    discount = 0
    after = 0

    if current >= trig:
        current -= current * (percent / 100)
    if sums >= trig:
        discount = sums * (percent/100)
        after = sums - discount
        if after == current:
            print("Yes")
        elif current > after:
            print(f"Yes {abs(current - (sums - discount)):.3f}")
        elif current < after:
            print(f"No {abs(current - (sums - discount)):.3f}")
    else:
        print("Yes")
main()
