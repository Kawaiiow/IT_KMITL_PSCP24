"""Sick"""

def main() -> None :
    """void"""
    t = float(input())

    if t >= 40:
        print("Very High Fever")
    elif t >= 39:
        print("High Fever")
    elif t >= 38:
        print("Mild Fever")
    else:
        print("No Fever")
main()
