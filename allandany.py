_, l = input(), input().split()
positive = all([int(i) >= 0 for i in l])
pallindromic = any([''.join(reversed(i)) == i for i in l])
print(positive and pallindromic)