"""Up to the heaven"""

def main(h, n):
    """void"""
    sums = 0
    tmp = 0
    step = 0
    state = 1

    for _ in range(n):
        step = int(input())
        tmp += step
        if step > h:
            state = 0
        if tmp == h:
            tmp = 0
            sums += 1
        elif tmp > h:
            sums += 1
            tmp = step
    if tmp > 0:
        sums += 1
    if not state:
        print("NO")
    else:
        print(sums)
main(int(input()),int(input()))
