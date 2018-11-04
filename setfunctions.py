input()
numbers = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    inp = input().split()
    command = inp[0]
    try:
        num = inp[1]
    except:
        pass
    if command == 'pop':
        try:
            numbers.pop()
        except:
            pass
    elif command == 'remove':
        try:
            numbers.remove(int(num))
        except:
            pass
    elif command == 'discard':
        numbers.discard(int(num))
    
print(sum(numbers))