from collections import deque

numbers = deque()
n = int(input())
for _ in range(n):
    inp = input().split()
    command = inp[0]
    try:
        num = inp[1]
    except:
        pass
    if command == 'append':
        numbers.append(num)
    elif command == 'appendleft':
        numbers.appendleft(num)
    elif command == 'pop':
        numbers.pop()
    elif command == 'popleft':
        numbers.popleft()

print(' '.join(numbers))