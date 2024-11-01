"""middle point"""

def main() -> None :
    """void"""
    point = [ int(input()) for _ in range (3) ]
    point.sort()
    diff = [ abs(point[i] - point[i + 1]) for i in range (2) ]
    print(max(diff) - 1)
main()
