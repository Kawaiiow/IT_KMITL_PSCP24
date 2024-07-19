"""Grade A"""
import math

def main():
    """void"""
    c = int(input())
    sums_point = 0
    for _ in range(c):
        sums_point += float(input()[:-1])

    sums_point /= c

    if 95 <= sums_point <= 100:
        print("4.00")
    if 90 <= sums_point < 95:
        print("3.50")
    if 85 <= sums_point < 90:
        print("3.00")
    if 80 <= sums_point < 85:
        print("2.50")
    if 75 <= sums_point < 80:
        print("2.00")
    if 70 <= sums_point < 75:
        print("1.50")
    if 65 <= sums_point < 70:
        print("1.00")
    if 60 <= sums_point < 65:
        print("0.50")
    else:
        print("0.00")
# main()

a = 10.417123124
a = float(str(a)[:-1])
print(f"{a}")
