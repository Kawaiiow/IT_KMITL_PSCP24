"""Test"""

def parser() -> str:
    """void"""
    res = ""

    for _ in range (8):
        buffer = input()
        res += "1" if buffer == "on" else "0"
    return res

def parse_number(msg):
    """int"""
    res = 0

    if msg == "1111110":
        res = 0
    elif msg == "0110000":
        res = 1
    elif msg == "1101101":
        res = 2
    elif msg == "1111001":
        res = 3
    elif msg == "0110011":
        res = 4
    elif msg == "1011011":
        res = 5
    elif msg == "1011111":
        res = 6
    elif msg == "1110000":
        res = 7
    elif msg == "1111111":
        res = 8
    elif msg == "1111011":
        res = 9
    else:
        res = -1
    return res

def main() -> None :
    """void"""
    bit_n1 = parser()
    bit_n2 = parser()
    bit_n3 = parser()
    float_bit = bit_n1[-1] + bit_n2[-1] + bit_n3[-1]
    if float_bit.count("1") > 1:
        print("Error")
        return
    float_point = float_bit.find("1") + 1
    bit_n1 = parse_number(bit_n1[:-1])
    bit_n2 = parse_number(bit_n2[:-1])
    bit_n3 = parse_number(bit_n3[:-1])
    if -1 in (bit_n1, bit_n2, bit_n3):
        print("Error")
        return
    if not float_point or float_point == 3:
        print(f"{(bit_n1 * 100) + (bit_n2 * 10) + bit_n3}.00")
    elif float_point == 2:
        print(f"{(bit_n1 * 10) + bit_n2}.{bit_n3}0")
    elif float_point == 1:
        print(f"{bit_n1}.{bit_n2}{bit_n3}")
main()
