"""admin12345"""
import math
import re

def check_entropy(msg):
    """calculate entropy"""
    entropy = 0

    if re.search(r"([a-z])", msg):
        entropy += 26
    if re.search(r"([A-Z])", msg):
        entropy += 26
    if re.search(r"([0-9])", msg):
        entropy += 10
    if re.search(r"([^a-zA-Z0-9])", msg):
        entropy += 32
    return entropy


def main():
    """void"""
    msg = input()
    entropy = check_entropy(msg)

    entropy = int(math.log2(entropy ** len(msg)))
    print(entropy)
    if entropy >= 128:
        print("Very Strong")
    elif entropy >= 60:
        print("Strong")
    elif entropy >= 36:
        print("Reasonable")
    elif entropy >= 28:
        print("Weak")
    else:
        print("Very Weak")
main()
