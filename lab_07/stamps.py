"""stamps"""

def main():
    """void"""
    n = int(input())
    target_price = int(input())
    get_stamp = int(input())
    ex_rate = int(input())
    discount = int(input())
    total_spend = 0
    stamps = 0

    for _ in range(n):
        bill_price = int(input())
        while stamps >= ex_rate and bill_price > 0:
            bill_price -= discount
            stamps -= ex_rate
        if bill_price < 0:
            bill_price = 0
        if bill_price >= target_price:
            stamps += get_stamp * (bill_price // target_price)
        total_spend += bill_price
    print(total_spend)
    print(stamps)
main()
