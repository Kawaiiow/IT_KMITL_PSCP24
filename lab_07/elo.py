"""Competitive"""

def main():
    """void"""
    ra = int(input())
    rb = int(input())
    flag = input()
    diff = 0

    if flag == 'A':
        diff = rb - ra
    else:
        diff = ra - rb
    print(f"{1 / (1 + 10 ** (diff / 400)):.2f}")
main()
