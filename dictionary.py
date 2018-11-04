from collections import defaultdict, Counter
dictionary = defaultdict(list)
b = []
[n, m] = map(int, input().split())
for i in range(n):
    dictionary[input()].append(i + 1)
for i in range(m):
    b.append(input())

for i in b:
    if i in dictionary:
        print(' '.join(map(str, dictionary[i])))
    else:
        print(-1)