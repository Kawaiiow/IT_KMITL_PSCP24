"""so-longggggggg"""

def main():
    """void"""
    num = int(input())
    step = 0
    str_buffer = ""
    cur_buffer = num
    low_buffer = num

    while cur_buffer != -1:
        temp = int(input())
        if temp - 1 == cur_buffer:
            step += 1
            cur_buffer = temp
        else:
            if cur_buffer != low_buffer:
                str_buffer += str(low_buffer) + "-" + str(cur_buffer)
            else:
                str_buffer += str(low_buffer)
            if temp != -1:
                str_buffer += ", "
            low_buffer = temp
            cur_buffer = temp
    print(str_buffer)
main()
