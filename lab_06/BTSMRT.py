"""BTS"""
def main():
    """MRT"""
    day = input()
    age = float(input())
    height = float(input())
    if day == "Senior Day" and age >= 60:
        print("FREE")
    elif day == "Children Day" and age < 14 and  90 <= height <= 140:
        print("FREE")
    elif age < 14 and height < 90:
        print("FREE")
    else:
        print("PAY")
main()
