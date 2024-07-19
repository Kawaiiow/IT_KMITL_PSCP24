"""mod doc"""
def main():
    """doc"""
    x= int(input())
    count = 1
    for i in range(x,0,-1):
        print(i, end=" ")
        if not count %7 and count:
            print()
        count +=1
main()
