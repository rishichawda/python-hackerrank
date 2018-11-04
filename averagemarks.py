if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_score = student_marks[query_name]
    average = sum(student_score) / 3.00
    print('{0:.2f}'.format(average))