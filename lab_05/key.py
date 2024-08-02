"""key"""

def main():
    """void"""
    key = input()
    keysums = 0

    for i in range(13):
        keysums += int(key[i])
    keysums += int(key[-3:]) * 10
    if keysums > 9999:
        print(str(keysums)[-4:])
    elif keysums < 1000:
        print(keysums + 1000)
    else:
        print(keysums)
main()
