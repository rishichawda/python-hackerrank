n = int(input())
integer_list = map(int, input().split())
num = tuple(integer_list)
print(hash(num))