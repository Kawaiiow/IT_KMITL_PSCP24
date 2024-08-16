"""rope of fortune"""

def main():
    """void"""
    a_force = 0
    b_force = 0

    for _ in range(10):
        a_force += int(input())
    for _ in range(10):
        b_force += int(input())

    if a_force > b_force:
        print("B")
    elif a_force < b_force:
        print("A")
    else:
        print("AB")
main()
