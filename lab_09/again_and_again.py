"""Again?"""

def syn(word) -> None :
    """bool"""
    char_set = ['a', 'e', 'i', 'o', 'u']
    occur = 0

    for c in word:
        if c in char_set:
            occur += 1
        if occur == 2:
            return True
    return False

def main() -> None :
    """void"""
    msg : str = input().replace(".", "")
    res: list = list(filter(syn, msg.split()))

    if res:
        print(*sorted(res), sep="\n")
    else:
        print("Nope")
main()
