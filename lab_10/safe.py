"""VAULT"""

def main() -> None :
    """void"""
    src = input()
    dst = input()
    sum_move = 0

    for c, _ in enumerate(src):
        s_chr = ord(src[c])
        d_chr = ord(dst[c])
        if 0 < abs(d_chr - s_chr) <= 13:
            sum_move += abs(d_chr - s_chr)
        elif abs(d_chr - s_chr) > 13:
            sum_move += min(abs(ord('A') - d_chr), abs(ord('Z') - d_chr)) + \
                        min(abs(ord('A') - s_chr), abs(ord('Z') - s_chr)) + 1
    print(sum_move)
main()
