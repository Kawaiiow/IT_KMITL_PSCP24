"""Tax time.. how much? Just guess.."""

def unsigned_range(n):
    """int"""
    if n <= 0:
        return 0
    return n

def main():
    """void"""
    sal = int(input())
    remainer = 0
    tax = 0

    tax += unsigned_range(sal - 4000000) * 0.35
    remainer += unsigned_range(sal - (4000000 + remainer))
    tax += unsigned_range(sal - (2000000 + remainer)) * 0.30
    remainer += unsigned_range(sal - (2000000 + remainer))
    tax += unsigned_range(sal - (1000000 + remainer)) * 0.25
    remainer += unsigned_range(sal - (1000000 + remainer))
    tax += unsigned_range(sal - (750000 + remainer)) * 0.20
    remainer += unsigned_range(sal - (750000 + remainer))
    tax += unsigned_range(sal - (500000 + remainer))* 0.15
    remainer += unsigned_range(sal - (500000 + remainer))
    tax += unsigned_range(sal - (300000 + remainer))* 0.10
    remainer += unsigned_range(sal - (300000 + remainer))
    tax += unsigned_range(sal - (150000 + remainer))* 0.05
    print(int(tax))
main()
