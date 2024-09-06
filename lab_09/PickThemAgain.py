"""PickThemAgain"""
def main():
    """PickThemAgain"""
    x = input().split(" ")
    x = list(map(int,x))
    y = len(x)
    z = 0
    for i in range(y-1,-1,-1):
        if not x[i] %3 or  not x[i] %5:
            print(x[i])
            z =1
    if not z :
        print("Nope")
main()
