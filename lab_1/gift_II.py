"""odd add odd add"""

def diff(n):
    """void"""
    if not n % 2:
        print(n)


def main():
    """void"""
    mem = [None] * 8
    for i in range(8):
        mem[i] = int(input())
    for j in range(8):
        diff(mem[j])
main()
