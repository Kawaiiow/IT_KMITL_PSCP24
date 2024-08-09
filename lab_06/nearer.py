"""nearer"""
def main():
    """nearer"""
    AlicePos = int(input())
    BobPos = int(input())
    TruckPos = int(input())
    if abs(TruckPos-AlicePos) > abs(TruckPos-BobPos):
        print("Bob", abs(TruckPos-BobPos))
    elif abs(TruckPos-AlicePos) < abs(TruckPos-BobPos):
        print("Alice", abs(TruckPos-AlicePos))
    else:
        print("Sundaes", abs(TruckPos-AlicePos))
main()
