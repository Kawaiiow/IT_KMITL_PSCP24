"""timing"""


def main():
    """timing"""
    n = int(input())
    mins = n // 60
    sec = n % 60
    sec = sec%60
    hrs = mins//60
    mins = mins%60
    days = hrs//24
    hrs = hrs%24
    if days > 9999:
        print("ERR_:__:__:__")
    else :
        print(f"{days:04}:{hrs:02}:{mins:02}:{sec:02}")
main()
