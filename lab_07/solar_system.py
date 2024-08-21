"""Solar Ray"""

def clean_msg(msg):
    """str"""
    res = ""
    space_state = 0

    for i in msg:
        if i != " ":
            space_state = 0
            res += i
        elif i == " " and not space_state:
            space_state = 1
            res += " "
        elif i == " " and space_state:
            res += ""
    return res

def get_hard_left(msg):
    """str"""
    res = ""
    i = 0

    while msg[i] != " ":
        res += msg[i]
        i += 1
    return res

def get_hard_right(msg):
    """str"""
    res = ""

    for i in range(msg.rindex(" ") + 1, len(msg)):
        res += msg[i]
    return res

def get_sun_left(msg, code):
    """str"""
    end_point = msg.rfind(code)
    start = msg.rfind(" ", 0, end_point) + 1 if msg.rfind(" ", 0, end_point) else 0
    res = ""

    for i in range(start, end_point):
        res += msg[i]
    return res

def get_sun_right(msg, code):
    """str"""
    res = ""
    start = msg.find(code) + len(code)
    end = msg.find(" ", start) if msg.find(" ", start) != -1 else len(msg)

    for i in range(start, end):
        res += msg[i]
    return res

def get_sun_index(msg, n):
    """int"""
    pos = 0
    if msg.find(" Sun ") > -1:
        sun_raw = msg.index(" Sun ")
        r_padding = msg[sun_raw + 4:].count(" ")
        pos = n - r_padding
    elif msg[:4] == "Sun ":
        pos = 0
    elif msg [-4:] == " Sun":
        pos = n

    return pos

def main():
    """void"""
    msg = clean_msg(input().strip())
    planet_count = msg.count(" ")
    sun_index = get_sun_index(msg, planet_count)
    hot = ""
    cool = ""

    if sun_index == planet_count / 2:
        hot += get_sun_left(msg, " Sun ") + " "
        hot += get_sun_right(msg, " Sun ")
        cool += get_hard_left(msg) + " "
        cool += get_hard_right(msg)
    else:
        if sun_index and sun_index != planet_count:
            hot += get_sun_left(msg, " Sun ") + " "
            hot += get_sun_right(msg, " Sun ")
        elif not sun_index:
            hot += get_sun_right(msg, "Sun ")
        elif sun_index == planet_count:
            # Mark where thing fuck up
            hot += get_sun_left(msg, " Sun")
        if sun_index < planet_count / 2:
            cool += get_hard_right(msg)
        if sun_index > planet_count / 2:
            cool += get_hard_left(msg)
    print("Hot:",hot)
    print("Cool:",cool)
main()
