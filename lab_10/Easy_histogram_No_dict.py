"""Easy Histogram"""

def parse(u_chr, u_cnt, l_chr, l_cnt):
    """void"""
    l_index = 0
    u_index = 0

    for i in range (26):
        if l_chr.count(chr(97 + i)):
            print(f"{l_chr[l_index]} = {l_cnt[l_index]}")
            l_index += 1
        if u_chr.count(chr(65 + i)):
            print(f"{u_chr[u_index]} = {u_cnt[u_index]}")
            u_index += 1

def nmain():
    """void"""
    msg = sorted(input().replace(" ", ""))
    l_chr = []
    u_chr = []
    l_cnt = []
    u_cnt = []
    l_index = 0
    u_index = 0
    buffer = ""

    for c in msg:
        if c.isupper():
            buffer = '' if buffer.islower() else buffer
            if buffer == c:
                u_cnt[u_index] += 1
            elif not buffer:
                buffer = c
                u_chr.append(buffer)
                u_cnt.append(0)
                u_cnt[u_index] += 1
            else:
                buffer = c
                u_chr.append(buffer)
                u_index += 1
                u_cnt.append(0)
                u_cnt[u_index] += 1
        else:
            buffer = '' if buffer.isupper() else buffer
            if buffer == c:
                l_cnt[l_index] += 1
            elif not buffer:
                buffer = c
                l_chr.append(buffer)
                l_cnt.append(0)
                l_cnt[l_index] += 1
            else:
                buffer = c
                l_chr.append(buffer)
                l_index += 1
                l_cnt.append(0)
                l_cnt[l_index] += 1
    parse(u_chr, u_cnt, l_chr, l_cnt)
nmain()
