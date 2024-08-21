"""book"""
import math

def main():
    """void"""
    n = int(input())
    ppb = int(input())
    x = int(input())
    y = int(input())
    time_spend = 0
    rpd = 0
    read = 0

    while n and rpd < ppb:
        rpd = math.ceil(ppb * (x / y))
        read += rpd
        if read >= ppb:
            n -= 1
            read = 0
        x += 1
        y += 1
        time_spend += 1
    time_spend += n
    print(time_spend)
main()
