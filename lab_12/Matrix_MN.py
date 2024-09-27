"""Matrix_MN"""
def main():
    """mainnnn"""
    m = int(input())
    n = int(input())
    lis = []
    for _ in range(m):
        buf = ""
        for _ in range(n):
            a = input()
            buf += a + " "
        lis.append(buf)
    print(*lis, sep="\n", end ="")
main()

# s1 = "Hello"
# s2 = "world"
# print(s1, s2, sep="\n", end="")
