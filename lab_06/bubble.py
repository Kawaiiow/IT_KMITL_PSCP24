"""Buuble Sort isn't way to go to"""

def check_path(msg):
    """void"""
    move_pos = 0

    if msg[0] in ('^', 'o'):
        move_pos += small_bubble(msg[1])
    elif msg[0] == "O":
        move_pos += big_bubble(msg[1:4])
    # print(msg)
    return move_pos

def small_bubble(msg):
    """int"""
    if not msg in ('o', 'O', '|', '^'):
        return 0
    return 1

def big_bubble(msg):
    """void"""
    pos = 0
    best = 0

    if msg == "   ":
        return 0
    for i in range(len(msg) - 1 , -1, -1):
        if msg[i] == "|" and not best:
            pos = i
            best = 1
        elif msg [i] == "O" and not best:
            pos = i
            best = 1
        elif msg[i] == "o" and i > pos and not best:
            pos = i
    return pos + 1

def main():
    """void"""
    msg = input()
    i = 0
    pos = 0
    temp = 0
    move_state = 1
    finish = 0

    while move_state and not finish:
        temp = pos
        pos += check_path(msg[pos:])
        if temp == pos:
            move_state = 0
        if msg[pos] == '|':
            finish = 1
        i += 1
    print("POSSIBLE" if finish else "IMPOSSIBLE")
    print(i if finish else len(msg) - (pos + 1))
main()
