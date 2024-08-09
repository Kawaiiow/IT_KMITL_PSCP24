"""bigger frame"""

def main():
    """void"""
    txt_1 = input().strip()
    txt_2 = input().strip()
    txt_3 = input().strip()
    txt_4 = input().strip()
    txt_5 = input().strip()

    length = max(len(txt_1), len(txt_2), len(txt_3), len(txt_4), len(txt_5))
    print("*"*(length + 4))
    print("* "+ txt_1.ljust(length) +" *")
    print("* "+ txt_2.ljust(length) +" *")
    print("* "+ txt_3.ljust(length) +" *")
    print("* "+ txt_4.ljust(length) +" *")
    print("* "+ txt_5.ljust(length) +" *")
    print("*"*(length + 4))
main()
