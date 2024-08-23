"""Buuble Sort isn't way to go to"""

def check_path(msg):
    """void"""
    move_pos = 0

    if msg[0] == 'o':
        move_pos += small_bubble(msg[1])
    elif msg[0] == "O":
        # print("Enter big")
        # print(msg[1:4])
        move_pos += big_bubble(msg[1:4])
    return move_pos

def small_bubble(msg):
    """int"""
    if not msg in ('o', 'O'):
        return 0
    return 1

def big_bubble(msg):
    """void"""
    pos = 0
    best = 0
    back = 3

    print(msg)
    if msg == "   ":
        return 0
    for i in range(len(msg) - 1 , -1, -1):
        # print(msg[i])
        if msg[i] == " ":
            continue
        elif msg[i] == "o" and i > pos and not best:
            pos = i
        elif msg [i] == "O" and not best:
            pos = i
            best = 1
    # print(pos)
    return pos + 1

def main():
    """void"""
    msg = input()
    pos = 0
    move_state = 1
    finish = 0

    while move_state and not finish:
        check_path(msg[pos:])

def test():
    """void"""
    a = "oOO"
    while 
    print(pos, a[pos])
test()
