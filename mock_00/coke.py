"""Coca Cola"""

def main():
    """void"""
    price = int(input())
    ex_rate = int(input())
    discount = int(input())
    target = int(input())
    total = price * target
    bundle = 0
    bottle = 0

    if ex_rate and target:
        bundle = target // ex_rate
        bottle = bundle * (ex_rate - 1)
        total = bottle * price
        bottle += bundle
        total += bundle * discount
        bottle += 1
        total += price
        if bottle < target:
            total += (target - bottle) * price
            bottle += target - bottle
        elif bottle > target:
            total -= (bottle - target) * discount
        print(total)
    else:
        print(total)
main()
