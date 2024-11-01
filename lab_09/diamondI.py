"""TIME TO GO TO AFRICA"""

def main() -> None :
    """void"""
    depth : int = int(input())
    width : int = int(input())
    res = [0] * width

    for _ in range (depth):
        buffer = list(map(int, input().split(" ")))
        for i in range (width):
            res[i] += buffer[i]
    print(max(res))
main()
