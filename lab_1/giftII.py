"""odd add odd add"""

def diff(n):
    """lorem ipsum"""
    if not n % 2:
        print(n)


def main():
    """crun"""
    mem = [None] * 8
    for i in range(8):
        mem[i] = int(input())
    for j in range(8):
        diff(mem[j])
main()
