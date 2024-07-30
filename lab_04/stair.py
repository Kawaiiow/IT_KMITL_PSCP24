"""Up to the heaven"""
import math

def main(h, n):
    """void"""
    sums = 0
    step = 0
    state = 1

    for _ in range(n):
        step = int(input())
        if step > h:
            state = 0
        sums += step
    if not h and not sums:
        print("1")
        return
    if not state:
        print("NO")
    else:
        print(f"{math.ceil(sums/h):.0f}")
main(int(input()),int(input()))

