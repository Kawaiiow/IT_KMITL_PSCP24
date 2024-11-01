"we seek for truth"
import re

def main() -> None:
    """void"""
    num = re.findall(r"([0-9]+)", input())
    num = list(map(int, num))
    print(sum(num))
main()
