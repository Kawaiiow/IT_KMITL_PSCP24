"""Game"""

def main():
    """void"""
    a = int(input())
    b = int(input())
    a_stale = a % 3
    b_stale = b % 3

    if a_stale != b_stale:
        print("Error")
        return
    if a_stale < b_stale:
        print(a_stale)
    else:
        print(b_stale)
main()
