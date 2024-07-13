"""Truck San"""


def main():
    """void"""
    avrg = float(input())
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = (avrg * 4) - (n1 + n2 + n3)
    tol_d = avrg - (avrg * 0.5)
    tol_u = avrg + (avrg * 0.5)

    if n1 <= 0 or n2 <= 0 or n3 <= 0 or n4 <= 0 or avrg <= 0:
        return
    if avrg * 4 <= 15000 and tol_d <= n1 <= tol_u and tol_d <= n2 <= tol_u \
        and tol_d <= n3 <= tol_u and tol_d <= n4 <= tol_u:
        print(f"Pass {n4:.2f}")
    elif avrg * 4 > 15000:
        print("Overweight")
    else:
        print("Unbalance")
main()
