"""BIG O"""

def n_cmp(n1, n2):
    """int"""
    if n2 > n1:
        return n2
    return n1

def check_permu(n1, n2, n3):
    """int"""
    concat = n1 + n2 + n3
    top = int(concat)
    concat = n1 + n3 + n2
    top = n_cmp(top, int(concat))
    concat = n2 + n1 + n3
    top = n_cmp(top, int(concat))
    concat = n2 + n3 + n1
    top = n_cmp(top, int(concat))
    concat = n3 + n1 + n2
    top = n_cmp(top, int(concat))
    concat = n3 + n2 + n1
    top = n_cmp(top, int(concat))
    return top


def main():
    """void"""
    x = str(input())
    y = str(input())
    z = str(input())
    top = check_permu(x, y, z)
    print(top)
main()
