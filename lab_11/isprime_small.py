"""Optimus prime"""

def is_prime(n) -> bool :
    """bool"""
    limit = n ** 0.5
    i = 2

    if n < 2:
        return False
    while i <= limit:
        if not n % i:
            return False
        i += 1
    return True

def main() -> None :
    """void"""
    print("Yes" if is_prime(int(input())) else "No")
main()
