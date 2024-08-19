"""WHAT THE FUCK IS KILOMETER!!!!!! RAHHHH!!!!"""

def label_out(head, body, tail):
    """void"""
    print(head, body)
    print(f"I-{tail % 100}")

def even_odd(n):
    """string"""
    if not n % 2:
        return "Even"
    return "Odd"

def main():
    """void"""
    number = int(input())
    head = ""

    if number < 100 and not number % 5 and number:
        if not number % 10:
            head = "Horizontal"
        elif number % 10 == 5:
            head = "Vertical"
        label_out(head, "Major Interstate", number)
    elif 100 < number < 1000 and not number % 5 and number % 100:
        label_out(even_odd(number // 100), "Minor Interstate", number)
    else:
        print("Others")
main()
