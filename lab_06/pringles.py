"""Potato Aim more like Skill Issue"""

def main():
    """void"""
    l_case = input()
    content = input()
    r_case = input()
    r = int(input())
    n = 0

    for i in range(r):
        if content[i] == ')':
            n += 1
    content = " "*r + content[r:]
    print(n)
    if content.find(')') >= 0:
        print("There are still some left.")
    else:
        print("None.")
    print(l_case)
    print(content)
    print(r_case)
main()
