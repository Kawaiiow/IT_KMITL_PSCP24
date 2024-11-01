"""MICROSOFT WORD II"""

def main() -> None :
    """void"""
    src = input()
    dst = input()
    buffer = ""
    long = len(max(src, dst, key=len))

    for i in range(long + 1):
        buffer = ""
        buffer += dst[:i]
        buffer += src[i:]
        print(buffer)
main()
