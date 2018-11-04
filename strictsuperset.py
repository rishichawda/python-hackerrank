set_A = set(input().split())
n = int(input())
ss = True
for _ in range(n):
    if set_A.issuperset(input().split()):
        pass
    else:
        ss = False
        break

print(ss)