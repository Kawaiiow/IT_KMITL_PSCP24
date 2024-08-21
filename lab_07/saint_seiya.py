"""Uhmm... no idea haven't watch it for long time"""

def main(time_limit, fist_limit):
    """void"""
    cur_time = 0
    limit_break = 0
    all_combos = 0
    atk = 0

    all_combos = time_limit // 6
    limit_break = fist_limit // 331
    atk += limit_break * 331 if limit_break < all_combos else all_combos * 331
    cur_time = int((atk / 331) * 6)
    while atk < fist_limit and cur_time // 2 < time_limit // 2:
        cur_time += 2
        atk += 165
    atk += 12 * (time_limit - cur_time - 1) if time_limit - cur_time - 1 > 0 else 0
    print(atk)
main(int(input()), int(input()))
