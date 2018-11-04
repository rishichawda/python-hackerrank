n = int(input())
list = []
for _ in range(n):
    statement = input().split()
    if statement[0] == 'insert':
        list.insert(int(statement[1]), int(statement[2]))
    elif statement[0] == 'print':
        print(list)
    elif statement[0] == 'remove':
        list.remove(int(statement[1]))
    elif statement[0] == 'append':
        list.append(int(statement[1]))
    elif statement[0] == 'sort':
        list = sorted(list)
    elif statement[0] == 'pop':
        list.pop()
    elif statement[0] == 'reverse':
        list = list[::-1]