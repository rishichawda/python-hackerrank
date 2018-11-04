from itertools import combinations

found = 0

input()
combination_list = list(combinations(list(input().split()), int(input())))
for combination in combination_list:
    print(list(combination))
    if 'a' in list(combination):
        found += 1

print('{0:.12f}'.format(found / len(combination_list)))