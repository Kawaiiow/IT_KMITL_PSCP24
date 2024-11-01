"""Someone is cheating"""

RANK = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def search(stack: list) -> None :
    """void"""
    sign = stack[0][-1]

    for c in RANK:
        if c + sign not in stack:
            print(c + sign)
            return

def main() -> None :
    """void"""
    count = [0, 0, 0, 0]
    s_stack = []
    h_stack = []
    d_stack = []
    c_stack = []

    for _ in range (51):
        msg = input()
        match msg[-1]:
            case "S":
                s_stack.append(msg)
                count[0] += 1
            case "H":
                h_stack.append(msg)
                count[1] += 1
            case "D":
                d_stack.append(msg)
                count[2] += 1
            case "C":
                c_stack.append(msg)
                count[3] += 1
            case _:
                print("error")
    for i in range(4):
        match count[i]:
            case 13:
                continue
            case _:
                match i:
                    case 0:
                        search(s_stack)
                    case 1:
                        search(h_stack)
                    case 2:
                        search(d_stack)
                    case 3:
                        search(c_stack)
                return
main()
