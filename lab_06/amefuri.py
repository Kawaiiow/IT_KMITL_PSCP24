"""Fun fat : The day you washing your clothes is going to be rainy day"""

def decoder(c):
    """int"""
    buffer = 0

    if c == 'c':
        buffer = -0.5
    elif c == 'n':
        buffer = -1
    elif c == 'w':
        buffer = -1.5
    elif c == 'r':
        buffer = 2
    elif c == 's':
        buffer = 3
    return buffer

def main():
    """void""" 
    time = int(input())
    w_code = input().lower()
    factor = 1
    presence = 1
    level = 8
    for i in w_code:
        if level > 16:
            level = 16
        elif not level:
            break
        factor = 1 if 6 <= time < 18 else 0.5
        if i in ('r', 's'):
            level += decoder(i)
        elif i in ('c', 'n', 'w'):
            level += decoder(i) * factor
        else:
            presence = 0
            break
        time += 1
        time = 0 if time == 24 else time
    if not presence:
        print("Lost")
    elif level:
        print(f"Still Wet (Wet Level: {level:.2f})")
    else:
        print("Dry")
main()
