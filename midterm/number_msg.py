"""encrypt"""

def decode(c):
    """char"""
    res = ''

    if c == '0':
        res = 'O'
    elif c == "1":
        res = 'I'
    elif c == "3":
        res = 'E'
    elif c == "4":
        res = 'A'
    elif c == "5":
        res = 'S'
    else:
        res = c
    return res

def main():
    """run encode"""
    msg = input()
    res = ""
    msg = msg.replace("12", "R")
    msg = msg.replace("13", "B")

    for i in msg:
        res += decode(i)
    res = res.upper()
    temp = res
    res = ""
    for i in temp:
        if not i in ("0", "1", "2", "3", "4", '5', '6' , '7', '8' , '9'):
            res += i
    print(res.upper())
main()
