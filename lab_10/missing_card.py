"""Missing"""
COMP = {'QD', '5C', '8H', '6S', 'JS', 'JH', '4D', '6D', 'AS', '5H', '2D', \
        'QC', '4C', '3S', '10D', '10C', '7H', 'KH', 'AC', '10H', 'QS', '5S',\
        '9S', '6C', 'JC', '8C', '2C', '9D', '3D', '7D', '4S', '9H', '10S', '2H',\
        'KS', '3C', 'QH', 'AD', 'KC', '7C', '9C', '3H', '8S', '4H', 'JD', '5D',\
        '2S', '7S', '8D', '6H', 'AH', 'KD'}


def main() -> None :
    """void"""
    stack = { input() for _ in range (51) }

    print(*(COMP - stack))
main()
