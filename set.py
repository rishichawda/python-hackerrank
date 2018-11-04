input()
a = set(map(int, input().split()))
input()
b = set(map(int, input().split()))
for i in sorted(a.union(b).difference(a.intersection(b))):
    print(i)