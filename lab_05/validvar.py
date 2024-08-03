"""INVALID READ"""

def isreserve(strs):
    """int"""
    if strs in ("if", "else", "elif", "while", "for", \
                "True", "False", "continue", "break", \
                "return", "is", "in", "and", "or", "from", \
                "as", "pass", "not", "def", "None", ""):
        return 1
    return 0

def main():
    """void"""
    n = int(input())
    cache = ""

    for _ in range(n):
        buffer = input()

        buffer = buffer.strip()
        if buffer.isidentifier() and not isreserve(buffer) :
            cache += "1"
        else:
            cache += "0"
    for i in cache:
        if i == "1":
            print("Valid")
        else:
            print("Invalid")
main()
