"""Run Forest! Run!!"""


def main():
    """void"""
    strs = input()
    n = int(input())

    if n <= 0:
        return
    while n:
        print(strs)
        n -= 1
main()
