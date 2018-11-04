import itertools

a = map(int, input().split())
b = map(int, input().split())

print(' '.join(map(str, list(itertools.product(a, b)))))