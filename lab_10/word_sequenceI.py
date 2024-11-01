"""WORD??"""

def main() -> None :
    """void"""
    msg : str = input()

    for i, _ in enumerate(msg):
        print(msg[:i + 1])
main()

cache = {}

def fibo(n):
    if cache[n]: return cache[n]
    if n <= 1: return n
    cache[n] = fibo(n - 1) + fibo(n - 2)
    return cache[n]
