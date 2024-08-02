"""rock"""

def main():
    """void"""
    strs = input()
    a = 0
    b = 0

    for i in range (0, len(strs), 2):
        buffer = strs[i:i+2]
        if buffer in ('PR', 'SP', 'RS'):
            a += 1
        elif buffer in ('RP', 'PS', 'SR'):
            b += 1
    if a > b:
        print("A win ",a,"-",b,sep="")
    elif b > a:
        print("B win ",b,"-",a,sep="")
    else:
        print("DRAW ",a,sep="")
main()
