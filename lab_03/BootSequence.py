"""mod doc"""
def main():
    """doc"""
    x =int(input())
    for i in range(1,x+1):
        if i < x:
            print(i, end="_")
        else:
            print(i, end="")
main()
