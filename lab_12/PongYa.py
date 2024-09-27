"""PongYa"""
def main():
    """main"""
    a = int(input())
    if not a % 3 or a % 10 == 3:
        print("PONG")
    else:
        print(a)
main()

# print(9 % 10)
# print(84 % 10)
# print(39 % 10)
# print(19 % 10)
# print(1234812319 % 10)
# print(34534519 % 10)
# print(3453419 % 10)
