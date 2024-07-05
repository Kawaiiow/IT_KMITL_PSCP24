"""func"""


def fx(x):
    """fx"""
    return x * 2


def gx(x):
    """gx"""
    return (x / 2) + 1

N = int(input())

print(f'{fx(gx(N)):.2f}')
print(f'{gx(fx(N)):.2f}')
