"""FIBO"""

CACHE = {}

def fibo(n):
    """int"""
    key = str(n)
    if key in CACHE:
        return CACHE.get(key)
    if n <= 1:
        return n
    CACHE.update({key : fibo(n - 1) + fibo(n - 2)})
    return CACHE.get(key)

def caller(full, left, amount, i):
    """void"""
    if i <= full:
        fibo(600 + amount)
        caller(full, left, amount + 600, i + 1)
    fibo(left)

def main() -> None :
    """void"""
    n : int = int(input())
    full_round = 0
    left = 0

    if n > 600:
        full_round = n // 600
        left = n % 600
    caller(full_round, left,0 , 1)
    print(fibo(n))
main()
