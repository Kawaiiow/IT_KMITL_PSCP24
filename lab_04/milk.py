"""When dad will come back?? he's just going to get some milk"""

def main():
    """void"""
    price = int(input())
    ex = int(input())
    free = int(input())
    budge = int(input())
    piece = budge // price
    cap = piece

    while ex and cap >= ex:
        piece += free * (cap // ex)
        cap += (free * (cap // ex)) - (ex * (cap // ex))
    print(piece)
main()
