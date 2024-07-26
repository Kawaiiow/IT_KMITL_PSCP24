"""Fizz"""

def main():
    """void"""
    n = int(input())

    for i in range(1,n + 1):
        if not i % 3 and not i % 5:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
main()
