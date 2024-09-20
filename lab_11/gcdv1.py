"""Divided"""

def main():
    """void"""
    num = [ int(input()) for i in range (2)]
    minimum = min(num)
    maximum = max(num)
    buffer = 0
    step = 1
    if not minimum:
        print(maximum)
        return
    buffer = minimum // step
    while maximum % buffer or minimum % buffer:
        buffer = minimum // step
        step += 1
    print(buffer)
main()
