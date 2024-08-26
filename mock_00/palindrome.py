"""down"""

def parse_time(time):
    """int"""
    res = 0

    for i in time:
        if i.isdigit():
            res *= 10
            res += int(i)
    return res

def main():
    """void"""
    n = int(input())
    time = input()
    time = parse_time(time)
    temp = 0
    if time >= 2400:
        temp = time // 100 - 24 if time // 100 > 24 else 0
        time = time % 100
        time += temp * 100
    if str(time) == str(time)[::-1] or not time % 10:
        time += 1

    while n:
        if time % 100 == 60:
            time -= 60
            time += 100
            # print(time)
            # print("pss")
        if time >= 2400:
            temp = time // 100 - 24 if time // 100 > 24 else 0
            time = time % 100
            time += temp * 100
        if time >= 100:
            if str(time) == str(time)[::-1]:
                print(f"{time//100}:{(time % 100):02}")
                n -= 1
        else:
            if not time % 10:
                print(f"{time//100}:{(time % 100):02}")
                n -= 1
        # print("a")
        time += 1
main()
