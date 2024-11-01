"""car"""

def main() -> None :
    """void"""
    msg = input()
    order: dict = {}
    idx = 1

    while msg != "END":
        if "IT'S A DOG" in msg:
            order.popitem()
            idx -= 1
        else:
            msg = msg.split(", ")
            for obj in msg:
                if not order.get(obj):
                    order.update({obj: {"index": idx, "count": 1}})
                else:
                    order.update({obj: {"index": order[obj]["index"], \
                                        "count": order[obj]["count"] + 1}})
                idx += 1
        msg = input()
    for name in sorted(order):
        print(f"{name} {order[name]["index"]} {order[name]["count"]}")
main()
