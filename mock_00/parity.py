"""Binary"""

def main():
    """void"""
    msg = input()
    flag = input()
    bit_on = 0

    for i in msg:
        bit_on += 1 if i == '1' else 0
    msg += '1' if (bit_on % 2 and flag == "Even") or (not bit_on % 2 and flag == "Odd") else '0'
    print(msg)
main()
