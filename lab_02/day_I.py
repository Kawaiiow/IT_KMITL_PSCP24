"""yeah"""


def main():
    """Y"""
    y = int(input())

    if not y % 4 and (y % 100 or (not y % 100 and not y % 400)):
        print("Yes")
    else:
        print("No")
main()
