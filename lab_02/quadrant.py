"""quadrant"""


def main():
    """Q"""
    x = int(input())
    y = int(input())

    if x > 0 and y > 0:
        print("Q1")
    elif x < 0 < y:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    elif y < 0 < x:
        print("Q4")
    elif not x and y:
        print("Y")
    elif not y and x:
        print("X")
    else:
        print("O")
main()
