"""shooting stars"""

def main():
    """void"""
    msg = input()
    comet = 0
    shooting_star = 0
    constellation = 0
    buffer = ""

    for i in msg:
        if len(buffer) == 2:
            buffer = buffer[1:]
            buffer += i
        else:
            buffer += i
        if buffer in ("~*", "*~"):
            buffer = ""
            comet += 1
        elif buffer == "*/":
            buffer = ""
            shooting_star += 1
        elif buffer == "**":
            buffer = ""
            constellation += 1
    if comet or shooting_star or constellation:
        print(f"constellation: {constellation}")
        print(f"comet: {comet}")
        print(f"shooting star: {shooting_star}")
    else:
        print("Tonight is a quiet night.")
main()
