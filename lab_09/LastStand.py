"""LastStand"""
def main():
    """LastStand"""
    x = input().replace("[","").replace("]","").split(",")
    for i in x:
        print(i[-1])
main()
