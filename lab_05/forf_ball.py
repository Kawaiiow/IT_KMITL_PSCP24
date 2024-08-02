"""We ball"""

def main():
    """void"""
    code = input()
    pos = 1

    for char in code:
        if char == "A" and (pos in (1, 2)):
            if pos == 1:
                pos = 2
            elif pos == 2:
                pos = 1
        elif char == "B" and (pos in (2, 3)):
            if pos == 2:
                pos = 3
            elif pos == 3:
                pos = 2
        elif char == "C" and (pos in (1, 3)):
            if pos == 1:
                pos = 3
            elif pos == 3:
                pos = 1
    print(pos)
main()
