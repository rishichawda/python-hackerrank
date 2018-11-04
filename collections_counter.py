from collections import Counter

n = int(input())
shoes = Counter(map(int, input().split()))
n_customers = int(input())
total = 0
for _ in range(n_customers):
    [shoe_size, money] = map(int, input().split())
    if shoes[shoe_size] > 0:
        shoes[shoe_size] -= 1
        total += money

print(total)