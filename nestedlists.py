nested_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    nested_list.append([name, score])
unique = []
for student in nested_list:
    if student[1] not in unique:
        unique.append(student[1])
unique = sorted(unique)
second_highest = unique[1]
match = []
for student in reversed(nested_list):
    if student[1] == second_highest:
        match.append(student[0])
for student in sorted(match):
    print(student)