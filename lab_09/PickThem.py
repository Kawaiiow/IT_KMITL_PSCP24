"""PickThem"""
def main():
    """PickThem"""
    x = input().replace("[","").replace("]","").replace(",","").split(" ")
    x = list(map(int,x))
    even = 0
    for i in x:
        if not i%2:
            print(i)
            even =1
    if not even:
        print("Nope")
main()
