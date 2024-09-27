"""Inverter"""
def main():
    """main"""
    a = input()
    b = ""
    for i in a:
        if i == "1":
            b += "0"
        else:
            b += "1"
    c = b.lstrip("0")
    print(c)
main()
