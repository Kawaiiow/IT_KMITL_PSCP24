"""Square"""

def main():
    """void"""
    size = int(input())
    n = int(input())

    for i in range(size):
        buffer = ""
        if not i or i == size - 1:
            buffer += "*" * size
        else:
            for j in range (0, size):
                if not j or j == size - 1:
                    buffer += "*"
                if j in (i , size - (i + 1)):
                    buffer += "*"
                elif j and j != size - 1:
                    buffer += " "
        if n > 1:
            tmp = " " + buffer
            buffer += tmp * (n - 1)
        print(buffer)
main()
