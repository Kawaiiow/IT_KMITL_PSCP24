"""Bus Bus Bus"""

def sauce(queue):
    """list"""
    return int(queue.split()[0])

def main() -> None :
    """void"""
    capa: int = int(input())
    busstop: int = int(input())
    stack: list = []
    lst_queue = []
    before = 0
    current = 0
    success = 0

    lst_queue = [ input() for _ in range (busstop) ]
    lst_queue.sort(key=sauce)
    for i in range(busstop):
        queue = lst_queue[i].split()
        stop = queue[0]
        queue = queue[1:]
        before = len(stack)
        stack = [d for d in stack if d != stop]
        current = len(stack)
        success += abs(before - current)
        space_left = capa - current
        j: int = 0
        while j < len(queue) and space_left:
            if i < int(queue[j]) <= busstop:
                stack.append(queue[j])
                space_left -= 1
            j += 1
    print(success)
main()
