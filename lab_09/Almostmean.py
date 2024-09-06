"""Mean"""

def main():
    """void"""
    n = int(input())
    stu_id = []
    marks = []
    buffer = []
    mean = 0
    index_2mean = 0
    highest = 0

    for i in range(n):
        buffer = input().split("\t")
        stu_id.append(buffer[0])
        marks.append(buffer[1])
    marks = list(map(float, marks))
    for i in marks:
        mean += i
    mean /= n
    for i in range(n):
        if marks[i] <= mean and marks[i] > highest:
            highest = marks[i]
            index_2mean = i
    print(f"{stu_id[index_2mean]}\t{highest}")
main()
