"""star"""
def main():
    """death"""
    stars = input()
    a = stars.count("**")
    b = 0
    c = stars.count("*/")
    buffer = ""

    for i in stars:
        if len(buffer) == 2:
            buffer = buffer[1:]
            buffer += i
        else:
            buffer += i
        if buffer == "~*" or buffer == "*~":
            b += 1
            buffer = ""

    if a or b or c:
        print("constellation:",stars.count("**"))
        print("comet:",stars.count("~*")+stars.count("*~"))
        print("shooting star:",stars.count("*/"))
    else:
        print("Tonight is a quiet night.")
main()
