"""Parallel World"""

def main():
    """void"""
    text = input()
    size = len(text)

    for i in range(-size + 1, size, 1):
        if i < 0:
            print(text[:i].rjust(size))
        else:
            print(text[i:])
main()
