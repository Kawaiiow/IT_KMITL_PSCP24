"""Ascending Sort"""
def main():
    """Ascending Sort"""
    n = int(input())
    x = []
    for i in range(n):
        x.append(int(input()))
    x.sort()
    for i in x:
        print(i)
main()
