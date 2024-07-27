"""Starve"""

def main(n):
    """void"""
    min_price = float(input())
    min_weight = float(input())

    for _ in range(n - 1):
        tmp_price = float(input())
        tmp_weight = float(input())
        if tmp_weight / tmp_price > min_weight / min_price:
            min_price = tmp_price
            min_weight = tmp_weight
        elif tmp_weight / tmp_price == min_weight / min_price and \
            tmp_price < min_price:
            min_price = tmp_price
            min_weight = tmp_weight
    print(f"{min_price:.2f} {min_weight:.2f}")
main(int(input()))
