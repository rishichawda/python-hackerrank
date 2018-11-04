[n, x] = map(int, input().split())
marks = []
for _ in range(x):
    marks += [map(float, input().split())]
marks = zip(*marks)
for student in marks:
    print(sum(student)/x)