"""diamond"""

def main():
    """void"""
    n = int(input())

    for i in range((-n + 1) // 2, (n // 2) + 1, 1):
        buffer = ""
        if abs(i) == n // 2:
            buffer += ' '*abs(i) + '*'
        elif not i:
            buffer += '*'*n
        else:
            buffer += ' '*abs(i) + '*' + ' '*(((n//2) - abs(i)) + ((n//2) - abs(i)) - 1) + '*'
        print(buffer)
main()
