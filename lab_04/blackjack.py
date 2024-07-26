"""BJ"""


def solve(card, n):
    """solve"""
    res = []
    summary = 0
    for i in range(n):
        summary += int(card[i])
    res.append(summary)
    return res


def check_permu(card, n):
    """check every possible"""
    res = []
    if not card.count('A'):
        res = solve(card, n)
    else:
        a = 0
        for j in range(n):
            if card[(n - 1) - j] == 'A':
                if not a:
                    card.remove('A')
                    card.append("11")
                    a += 1
                else:
                    card.remove('A')
                    card.append("1")
        res = solve(card, n)
        card.remove("11")
        card.append("1")
        res += solve(card, n)
    return res


def call_card(n):
    """call before play"""
    hand = []
    while n:
        hand.append(input())
        n -= 1
    return hand


def point_convert(card):
    """we don't know how many point we have"""
    new = []
    n = 0
    while n < len(card):
        if card[n] == 'J' or card[n] == 'Q' or card[n] == 'K':
            new.append("10")
        else:
            new.append(card[n])
        n += 1
    return new


def play():
    """let's play"""
    res = []
    n = int(input())
    # if n != 2 or n != 3:
    #     return ;
    hand = call_card(n)
    # print(hand)
    hand = point_convert(hand)
    res = check_permu(hand, n)
    res.sort()
    temp = 0
    i = len(res) - 1
    while i >= 0:
        temp = res[i]
        if temp <= 21:
            break
        i -= 1
    print(temp)


play()
