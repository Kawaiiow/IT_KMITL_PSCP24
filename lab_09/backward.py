"""Backward"""
def main():
    """Backward"""
    text = input()
    x =[]
    while text != "NULL" :
        x.append(text)
        text = input()
    x.reverse()
    for i in x :
        print(i)
main()
