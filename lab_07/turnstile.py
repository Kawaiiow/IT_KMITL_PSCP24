"""You know automata theory??"""

def main():
    """void"""
    msg = input()
    state = 0
    count = 0

    while msg != "END":
        if msg == 'C':
            state = 1
        elif msg == 'P' and state == 1:
            count += 1
            state = 0
        msg = input()
    print(count)
main()
