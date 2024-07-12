"""triangle"""

def main():
    """45"""
    a = float(input())
    b = float(input())
    c = float(input())

    if a <= 0 or b <= 0 or c <= 0:
        print("No")
    elif 0 <= c**2 - (a**2 + b**2) <= 0.01:
        print("Yes")
    else:
        print("No")
main()
