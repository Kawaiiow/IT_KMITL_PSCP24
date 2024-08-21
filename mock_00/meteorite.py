"""Operation Meteor"""

def main():
    """void"""
    a = float(input())
    b = int(input())
    c = float(input())
    scatter = 0
    tree_count = 0
    shot = 0

    if a >= c and a:
        scatter = a / b
        shot += 1
        while scatter >= c:
            scatter /= b
            tree_count += 1
        for i in range(1, tree_count + 1):
            shot += b ** i
    print(shot)
main()
