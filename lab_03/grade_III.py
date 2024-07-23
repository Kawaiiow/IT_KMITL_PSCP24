"""Grade A"""


def point_cmp(n):
    """float"""
    point = 0
    if 95.00 <= n <= 100.00:
        point = 4.00
    elif 90.00 <= n < 95.00:
        point = 3.50
    elif 85.00 <= n < 90.00:
        point = 3.00
    elif 80.00 <= n < 85.00:
        point = 2.50
    elif 75.00 <= n < 80.00:
        point = 2.00
    elif 70.00 <= n < 75.00:
        point = 1.50
    elif 65.00 <= n < 70.00:
        point = 1.00
    elif 60.00 <= n < 65.00:
        point = 0.50
    else:
        point = 0.00
    return point


def main():
    """void"""
    c = int(input())
    sums_point = 0.00
    for _ in range(c):
        sums_point += point_cmp(float(input()))
    print(f"{(int(sums_point / c * 100) / 100):.2f}")
main()
