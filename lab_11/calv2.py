""" calV2 """
def cal():
    """ cal """
    st = int(input())
    buf = 0
    dig = 1
    if st == 1:
        print(1)
    else:
        while True:
            start = 10 ** (dig - 1)
            end = min(10 ** dig - 1, st)
            if start > st:
                break
            num_in = end - start + 1
            buf += num_in * dig
            dig += 1
        buf += st
        print(buf)
cal()
