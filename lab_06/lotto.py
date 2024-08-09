"""THAT"S A LOTTTTT!!!!!!!!"""

def six_ten_bound(n):
    """string"""
    buffer = str(n)

    if n < 0:
        buffer = "999999"
    elif n > 999999:
        buffer = "000000"
    buffer = '0'*(6 - len(buffer)) + buffer
    return buffer

def main():
    """void""" 
    first = input()
    b_double = input()
    first_f_tri = input()
    sec_f_tri = input()
    first_b_tri = input()
    sec_b_tri = input()
    target = input()
    prize_pool = 0

    if target == first:
        prize_pool += 6000000
    if target == six_ten_bound(int(first) - 1):
        prize_pool += 100000
    if target == six_ten_bound(int(first) + 1):
        prize_pool += 100000
    if target[:3] == first_f_tri:
        prize_pool += 4000
    if target[:3] == sec_f_tri:
        prize_pool += 4000
    if target[3:] == first_b_tri:
        prize_pool += 4000
    if target[3:] == sec_b_tri:
        prize_pool += 4000
    if target[4:] == b_double:
        prize_pool += 2000
    print(prize_pool)
main()
