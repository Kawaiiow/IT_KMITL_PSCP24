"""OWO"""

import math


# def ft_split(str, sep, n):
#     """Split Plus"""
#     i = 0
#     w = len(str)
#     print(w);
#     res = [None] * (n * 2)
#     j = 0
#     k = 0
#     p = 0
#     while i < w - 1:
#         while str[i] == sep and i < w - 1:
#             i += 1
#         if str[i] and i < w - 1:
#             j = i
#         while str[i] != sep and i < w - 1:
#             i += 1
#         if
#         k = i
#         # res.append(str[j:k])
#         print(p)
#         res[p] = (str[j:k])
#         p += 1;
#         print(i);
#     # print(f"{res}\n");
#     return res


def ft_substr(str, sep):
    k = 0
    i = 0
    w = len(str)
    n = 0
    while i < w - 1 and n < 1000:
        while str[i] == sep and i < w - 1:
            i += 1
        if str[i] and i < w - 1:
            n += 1
        while str[i] != sep and i < w - 1:
            i += 1
        k = i
        if not i < w - 1:
            k += 1
    return str[:k]


def sub_split(str, sep, n):
    res = []
    sub = math.ceil(n / 1000)
    print(sub)
    while sub:
        temp = ft_substr(str, sep)
        str = str[len(temp):]
        temp = temp.split(sep);
        res += temp
        sub -= 1;
    return res


def parse_int(arr, n):
    """owo"""
    new = [None] * (n * 2)
    print(f"arr len : {len(arr)}")
    for i in range((n * 2)):
        new.append(int(arr[i]))
    return new


def sail():
    """Kayak"""
    res = 0
    n = int(input())
    diff = [None] * n
    w = [None] * (n * 2);
    if n < 1:
        print("0")
    w = input()
    # print("\n\n\n\n")
    # print(w)
    # print(f"word len : {len(w)}")
    # w = sub_split(str, " ")
    # print("\n\n\n\n\n")
    # t = ft_substr(w, " ")
    # w = w[len(t):]
    t = sub_split(w, " ", (n * 2))
    # print(t);
    # print(f"len : {len(t)}")
    # print("\n\n\n\n\n")
    # print(len(t))
    # w = parse_int(w, n)
    # w.sort()
    # for i in range(0, (n * 2), 2):
    #     diff.append(w[i + 1] - w[i])
    # diff.sort()
    # for j in range(n - 1):
    #     res += diff[j]
    # print(res)


sail()

