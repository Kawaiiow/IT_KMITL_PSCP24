"""time"""

def main():
    """time"""
    start = 492137954293754252786
    ms = start
    sec = ms//1000
    ms = ms%1000
    mins = sec//60
    sec = sec%60
    hrs = mins//60
    mins = mins%60
    d = hrs//24
    hrs = hrs%24
    print(f'{d} {hrs} {mins} {sec} {ms}')
main()
