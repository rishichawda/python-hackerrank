from collections import deque
input()
set_A = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    [command, num] = input().split()
    if command == 'intersection_update':
        set_A.intersection_update(map(int, input().split()))
    elif command == 'update':
        set_A.update(map(int, input().split()))
    elif command == 'symmetric_difference_update':
        set_A.symmetric_difference_update(map(int, input().split()))
    elif command == 'difference_update':
        set_A.difference_update(map(int, input().split()))

print(sum(set_A))