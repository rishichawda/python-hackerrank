from itertools import combinations_with_replacement

[string, length] = input().split()

for combination in combinations_with_replacement(sorted(list(string)), int(length)):
    print(''.join(list(combination)))
