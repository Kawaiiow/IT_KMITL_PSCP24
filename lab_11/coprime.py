"""Co prime"""

def main():
    """void"""
    num = [ int(input()) for i in range (2)]
    minimum = min(num)
    maximum = max(num)
    buffer = 0
    step = 1
    if not minimum:
        if maximum != 1:
            print("NO")
            print(maximum)
        else:
            print("YES")
            print(1)
        return
    buffer = minimum // step
    while maximum % buffer or minimum % buffer:
        buffer = minimum // step
        step += 1
    if buffer == 1:
        print("YES")
        print(1)
    else:
        print("NO")
        print(buffer)
main()
