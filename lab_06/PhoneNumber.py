"""PhoneNum"""
def main():
    """PhoneNum"""
    phoneNum = input()
    callType = input()
    if callType == "Domestic":
        if len(phoneNum) == 9:
            print(phoneNum[0],phoneNum[1:5],phoneNum[5:])
        elif len(phoneNum) == 10:
            print(phoneNum[:2],phoneNum[2:6],phoneNum[6:])
    elif callType == "International":
        phoneNum = "+66"+phoneNum[1:]
        if len(phoneNum) == 11:
            print(phoneNum[:3],phoneNum[3:7],phoneNum[7:])
        elif len(phoneNum) == 12:
            print(phoneNum[:4],phoneNum[4:8],phoneNum[8:])
main()
