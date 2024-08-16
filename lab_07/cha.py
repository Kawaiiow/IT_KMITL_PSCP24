"""Cha Cha Cha"""
import math
def main():
    """Cha Cha Cha"""
    day = int(input())
    income = 0
    for _ in range(day):
        hour = math.ceil(float(input()))
        income += hour * 8720
    print(income)
main()
