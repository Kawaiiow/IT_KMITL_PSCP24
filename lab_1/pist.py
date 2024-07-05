"""psit when pstand comin"""

def grade():
    """C++"""
    m = float(input())
    if m < 0 or m > 100:
        return
    if m >= 60:
        print("Pass")
    else:
        print("Fail")
grade()
