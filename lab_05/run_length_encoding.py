"""Encrypt"""

def main():
    """void"""
    msg = input()
    n = 0
    buffer = ""

    for i in msg:
        if not buffer:
            buffer = i
        if buffer and buffer != i:
            print(f"{n}{buffer}",end="")
            buffer = i
            n = 0
        if buffer == i:
            n += 1
    print(f"{n}{buffer}",end="")
main()
