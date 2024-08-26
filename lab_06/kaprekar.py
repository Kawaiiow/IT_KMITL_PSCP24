"""endless"""

def ascend(n1, n2):
    """int"""
    if n1 > n2:
        return 1
    return 0

def bubble_sauce(num, f):
    """int"""
    buffer = list(map(str, str(num)))

    for i in range(len(buffer) - 1):
        for j in range((len(buffer) - 1) - i):
            if f(buffer[j], buffer[j + 1]):
                temp = buffer[j]
                buffer[j] = buffer [j + 1]
                buffer[j + 1] = temp
    return buffer

def main(val, n=0):
    """void"""
    if val == 6174:
        return n
    val = str(val)
    val = ((4 - len(val)) * '0') + val
    low = "".join(bubble_sauce(val, ascend))
    high = int(low[::-1])
    low = int(low)
    value = high - low
    return main(value,n + 1)
print(main(input()))
