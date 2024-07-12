'''Grade II'''
def main():
    '''Grade II'''
    A= float(input())
    if A > 100 or A <0:
        print("ERR")
    else:
        if A>=95:
            print("A")
        elif 90<=A<95:
            print("B+")
        elif 85<=A<90:
            print("B")
        elif 80<=A<85:
            print("C+")
        elif 75<=A<80:
            print("C")
        elif 70<=A<75:
            print("D+")
        elif 65<=A<70:
            print("D")
        elif 60<=A<65:
            print("F+")
        else:
            print("F")
main()
