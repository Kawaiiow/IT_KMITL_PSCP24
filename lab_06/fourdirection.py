"""Four direction"""

CENTER_DOT = "  *  "
LINE_DOT = "*****"
SPREAD_TRI = "* * *"
GROUP_TRI = " *** "
L_DOT = " *   "
R_DOT = "   * "

def main():
    """void"""
    code = input()

    for i in range(5):
        buffer = ""
        for j in code:
            if i in (0, 4) or \
                (i == 3 and j == 'U') or (i == 1 and j =='D'):
                buffer += CENTER_DOT
            elif (i == 1 and j == 'U') or (i == 3 and j == 'D'):
                buffer += GROUP_TRI
            elif i == 2 and j in ('U', 'D'):
                buffer += SPREAD_TRI
            elif i == 2 and j in ('L', 'R'):
                buffer += LINE_DOT
            elif j == 'L' and i in (1, 3):
                buffer += L_DOT
            elif j == 'R' and i in (1, 3):
                buffer += R_DOT
            buffer += ' '
        print(buffer)
main()
