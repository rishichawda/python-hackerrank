n = int(input())
for _ in range(n):
    input()
    set_A = set(input().split())
    input()
    set_B = input().split()
    if len(set_A.difference(set_B)) > 0:
        print(False)
    else:
        print(True)