list = [0, 1]
n = int(input())

for i in range(2, n):
    list.append(list[i-1] + list[i-2])
list = [pow(x,3) for x in list]

print(list[:n])