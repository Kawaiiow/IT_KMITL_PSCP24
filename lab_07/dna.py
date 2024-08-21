"""You're not his father!!"""
import re

def gen_substr(strs):
    """char **"""
    n = len(strs)
    return {strs[i:j + 1] for i in range(n) for j in range(i,n)}

def main():
    """void"""
    msg_A = input()
    msg_B = input()
    res = ""

    if not re.search(r"[^ATCG]", msg_A) and not re.search(r"[^ATCG]", msg_B):
        sub_strA = gen_substr(msg_A)
        sub_strB = gen_substr(msg_B)
        if sub_strA & sub_strB:
            res = max(sub_strA & sub_strB, key=len)
        print(res if res else "None")
    else:
        print("Error")
main()
