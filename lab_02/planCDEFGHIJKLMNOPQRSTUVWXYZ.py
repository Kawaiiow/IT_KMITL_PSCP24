"""plan"""

def n_cmp(n1, n2):
    """cmp"""
    if n1 > n2:
        return 1
    return 0

def main():
    """run"""
    method = input()
    x = float(input())
    y = float(input())
    z = float(input())

    if n_cmp(x, y):
        x = x + y
        y = x - y
        x = x - y
    if n_cmp(y, z):
        y = z + y
        z = y - z
        y = y - z
    if n_cmp(x, y):
        x = x + y
        y = x - y
        x = x - y

    if method == "Ascend":
        print(f"{x:.2f}, {y:.2f}, {z:.2f}")
    elif method == "Descend":
        print(f"{z:.2f}, {y:.2f}, {x:.2f}")
main()
