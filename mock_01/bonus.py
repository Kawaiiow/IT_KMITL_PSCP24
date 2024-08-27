"""Bonus"""

def main():
    """void"""
    salary = int(input())
    y = int(input())
    m = int(input())
    bonus = 5000

    if m >= 10:
        y += 1
    if y >= 20:
        y = 20
    if y:
        bonus = salary * y
        if bonus > 1000000:
            bonus = 1000000
        elif bonus < 5000:
            bonus = 5000
    print(bonus)
main()
