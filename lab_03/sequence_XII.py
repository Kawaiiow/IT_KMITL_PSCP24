"""XII"""

def main():
    """void"""
    n = int(input())

    for i in range(-n + 1, n, 1):
        for j in range(-n + 1, n, 1):
            print(f"{n - abs(abs(i) - abs(j)):02}" , end=" ")
        print()
main()
