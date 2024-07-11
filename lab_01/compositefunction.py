"""func"""


def fx(x):
    """int"""
    return x * 2


def gx(x):
    """int"""
    return (x / 2) + 1

N = int(input())

print(f'{fx(gx(N)):.2f}')
print(f'{gx(fx(N)):.2f}')
