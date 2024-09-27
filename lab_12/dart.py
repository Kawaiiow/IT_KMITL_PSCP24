"""DART"""

def point_cal(dis):
    """int"""
    m = 0
    if dis <= 2:
        m = 5
    elif dis <= 4:
        m = 4
    elif dis <= 6:
        m = 3
    elif dis <= 8:
        m = 2
    elif dis <= 10:
        m = 1
    return m

def point_dis(x, y):
    """int"""
    return ((x - 0)**2 + (y - 0)**2)**0.5

def main():
    """void"""
    n = int(input())
    total = 0

    for _ in range (n):
        pos = list(map(int, input().split(" ")))
        total += point_cal(point_dis(pos[0], pos[1]))
    print(total)
main()
