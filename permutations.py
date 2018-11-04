from itertools import permutations

[string, length] = input().split()

for per in sorted(list(permutations(string, int(length)))):
    print(''.join(list(per))) 