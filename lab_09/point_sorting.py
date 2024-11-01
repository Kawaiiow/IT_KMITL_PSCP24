"""Pointer*"""

def point_sorting() -> None:
    """void"""
    n: int = int(input())
    point = [ input() for _ in range(n) ]
    point = [{
                "x": int(obj.split()[0]),
                "y": int(obj.split()[1]),
                "sum": int(obj.split()[0]) + int(obj.split()[1])
            } for obj in point ]
    point = sorted(point, key=lambda s : (s["sum"], -s["y"]))
    for obj in point:
        print(obj["x"], obj["y"])

def main() -> None:
    """void"""
    n: int = int(input())

    for _ in range(n):
        point_sorting()
main()
