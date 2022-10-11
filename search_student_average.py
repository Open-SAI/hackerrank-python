if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    average = 0
    for x in student_marks.items():
        if x[0] == query_name:
            for p in x[1]:
                average += p
    print(format(float(average/3),".2f"))
