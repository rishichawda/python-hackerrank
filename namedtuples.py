from collections import namedtuple

n = int(input())
labels = input().split()
record = [int(input().split()[[int(i) for i in range(len(labels)) if labels[i] == 'MARKS'][0]]) for _ in range(n)]
print('{:.2f}'.format(sum(record) / n))