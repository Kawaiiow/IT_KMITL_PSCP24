"""VOLLEY"""

def main() -> None :
    """void"""
    msg = input()
    point_a, point_b, a_win, b_win, draw = (0, 0, 0, 0, 0)
    sets = 1

    for c in msg:
        point_a += 1 if c == 'A' else 0
        point_b += 1 if c == 'B' else 0

        if point_a == 24 and point_b == 24 and sets != 5:
            draw = 1
        if (point_b == 25 or point_a == 25) and not draw and sets != 5:
            print(f"Set {sets}: A ({point_a}) | B ({point_b})")
            a_win += 1 if point_a > point_b else 0
            b_win += 1 if point_b > point_a else 0
            point_b, point_a, sets = 0, 0, sets + 1
        if draw and abs(point_a - point_b) == 2 and sets != 5:
            print(f"Set {sets}: A ({point_a}) | B ({point_b})")
            a_win += 1 if point_a > point_b else 0
            b_win += 1 if point_b > point_a else 0
            point_b, point_a, sets, draw = 0, 0, sets + 1, 0
        if point_a == 14 and point_b == 14 and sets == 5:
            draw = 1
        if (point_b == 15 or point_a == 15) and not draw and sets == 5:
            print(f"Set {sets}: A ({point_a}) | B ({point_b})")
            a_win += 1 if point_a > point_b else 0
            b_win += 1 if point_b > point_a else 0
            point_b, point_a, sets = 0, 0, sets + 1
        if draw and abs(point_a - point_b) ==  2 and sets == 5:
            print(f"Set {sets}: A ({point_a}) | B ({point_b})")
            a_win += 1 if point_a > point_b else 0
            b_win += 1 if point_b > point_a else 0
            point_b, point_a, sets, draw = 0, 0, sets + 1, 0
        if a_win == 3 or b_win == 3:
            break
    if sets != 6 and a_win != 3 and b_win != 3:
        print(f"Set {sets}: A ({point_a}) | B ({point_b})")
    if a_win == 3:
        print(f"A won {a_win}:{b_win} set")
    elif b_win == 3:
        print(f"B won {b_win}:{a_win} set")
    else:
        print("The game has not finished yet.")
main()
