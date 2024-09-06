"""Line sorting"""

def main():
    """void"""
    n = int(input())
    msg = []

    for _ in range(n):
        msg.append(input())
    for i in sorted(msg, key=len):
        print(i)
main()
