"""saitama"""
import math
def main():
    """saitama"""
    push_up = int(input())
    sit_up = int(input())
    sq = int(input())
    run = int(input())
    push_up_perday = int(input())
    sit_up_perday = int(input())
    run_perday = int(input())
    sq_perday = int(input())
    count = math.ceil(push_up / push_up_perday)

    if math.ceil(sit_up / sit_up_perday) > count:
        count = math.ceil(sit_up / sit_up_perday)
    if math.ceil(sq / sq_perday) > count:
        count = math.ceil(sq / sq_perday)
    if math.ceil(run / run_perday) > count:
        count = math.ceil(run / run_perday)

    print(count)
main()
