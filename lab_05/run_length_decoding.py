"""Decrypt"""

def main():
    """void"""
    msg = input()
    n = 0
    buffer = ""

    for buffer in msg:
        if buffer in ('0','1','2','3','4','5','6','7','8','9'):
            n *= 10
            n += int(buffer)
        else:
            print(str(buffer)*n,end="")
            n = 0
    print(str(buffer)*n,end="")
main()
