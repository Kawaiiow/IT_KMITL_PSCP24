"""Don't forget to pay your taxes. Also not recommended not to mess with IRS."""
import re

def main():
    """void"""
    bank_account = float(input())
    pocket = float(input())
    fail_attemp = 0

    msg = input()
    while msg != "end" and fail_attemp != 3:
        state = re.search(r"^[WD]", msg).group()
        value = float(re.search(r"(\d+)([.](\d+))*", msg).group())
        if state == "W" and bank_account >= value and value:
            fail_attemp = 0
            bank_account -= value
            pocket += value
        elif state == "D" and pocket >= value and value:
            fail_attemp = 0
            bank_account += value
            pocket -= value
        else:
            fail_attemp += 1
        if fail_attemp != 3:
            msg = input()
    print(f"{bank_account:.2f}")
    print(f"{pocket:.2f}")
main()
