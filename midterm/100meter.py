"""Run"""

def cmp(n1, time1, n2, time2, n3, time3, n_cmp, time_cmp):
    """int"""
    if time_cmp < time1 or not time1:
        return n_cmp, time_cmp, n1, time1, n2, time2
    if time_cmp < time2 or not time2:
        return n1, time1, n_cmp, time_cmp, n2, time2
    if time_cmp < time3 or not time3:
        return n1, time1, n2, time2, n_cmp, time_cmp
    return n1, time1, n2, time2, n3, time3

def main():
    """time"""
    f = 0
    ft = 0
    s = 0
    st = 0
    t = 0
    tt = 0
    r1 = float(input())
    f, ft, s, st, t, tt = cmp(f, ft, s, st, t, tt, 1, r1)
    r2 = float(input())
    f, ft, s, st, t, tt = cmp(f, ft, s, st, t, tt, 2, r2)
    r3 = float(input())
    f, ft, s, st, t, tt = cmp(f, ft, s, st, t, tt, 3, r3)
    r4 = float(input())
    f, ft, s, st, t, tt = cmp(f, ft, s, st, t, tt, 4, r4)
    r5 = float(input())
    f, ft, s, st, t, tt = cmp(f, ft, s, st, t, tt, 5, r5)
    r6 = float(input())
    f, ft, s, st, t, tt = cmp(f, ft, s, st, t, tt, 6, r6)
    r7 = float(input())
    f, ft, s, st, t, tt = cmp(f, ft, s, st, t, tt, 7, r7)
    r8 = float(input())
    f, ft, s, st, t, tt = cmp(f, ft, s, st, t, tt, 8, r8)
    print(f,s,t)
main()
