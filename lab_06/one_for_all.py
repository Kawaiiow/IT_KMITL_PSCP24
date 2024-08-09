"""Uhm.. I"ve never watch it..."""

def main():
    """void"""
    n = int(input())
    buffer = ""

    for i in range(1, n + 1):
        buffer += input()
        if i == n:
            buffer += '_' + str(i)
        elif i % 2 == 1:
            buffer += '*'*i
        elif not i % 2:
            buffer += '-'*i
    print(buffer)
main()
