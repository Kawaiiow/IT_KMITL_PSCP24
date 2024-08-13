"""PL > ping"""
import re

def as_cmp(h, n):
    """int"""
    if n > h:
        return n
    return h

def des_cmp(l, n):
    """int"""
    if not l or l > n:
        return n
    return l

def grep_ip(cmd, header):
    """char *"""
    reg_ipv4 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    reg_ipv6 = r'\b(?:[a-fA-F0-9]{1,4}:){4}\:[a-fA-F0-9]{1,4}\b'
    res = ""

    if re.search(reg_ipv4, cmd) or re.search(reg_ipv6, cmd):
        res = re.search(reg_ipv4, cmd)
        if not res:
            res = re.search(reg_ipv6, cmd)
        res = res.group()
    else:
        res = re.search(reg_ipv4, header)
        if not res:
            res = re.search(reg_ipv6, header)
        res = res.group()
    return res


def get_response_time(msg):
    """int"""
    response_pattern = r"(?<=time)([^']\d*)"
    sign = (re.search(response_pattern, msg).group())[0]
    time = (re.search(response_pattern, msg).group())[1:]

    if sign == '<':
        return int(time) - 1
    return int(time)

def main():
    """void"""
    cmd = input()
    blank = input()
    blank += 'a'
    header = input()
    address = grep_ip(cmd, header)
    fail_attemp = 0
    sum_time = 0
    max_time = 0
    min_time = 0

    for _ in range(4):
        response = input()
        if response in ("Request timed out.", "General failure."):
            fail_attemp += 1
        else:
            buffer = get_response_time(response)
            sum_time += buffer
            max_time = as_cmp(max_time, buffer)
            min_time = des_cmp(min_time, buffer)
    print(f"Ping statistics for {address}:")
    print(f"    Packets: Sent = 4, Received = {4 - fail_attemp}",end="")
    print(f", Lost = {fail_attemp} ({int(100 * (fail_attemp/4))}% loss),")
    if fail_attemp != 4:
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {min_time}ms, Maximum = {max_time}ms, ",end="")
        print(f"Average = {sum_time // (4 - fail_attemp)}ms")
main()
