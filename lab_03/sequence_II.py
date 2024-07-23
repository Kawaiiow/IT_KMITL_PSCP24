"""II"""

def main():
    """void"""
    n = int(input())
    x = 0

    for i in range(0, n):
        x = x + (1 + (2 * i))
        print(x, end=" ")
main()
