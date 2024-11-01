"""Imposter"""

def main() -> None :
    """void"""
    m : int = int(input())
    n : int = int(input())
    f_group = { int(input()) for _ in range (m)}
    s_group = { int(input()) for _ in range (n)}

    if f_group & s_group:
        print(*sorted(f_group & s_group, reverse=True), sep='\n')
    else:
        print("Nope")
main()
