from collections import OrderedDict

n = int(input())
dictionary = OrderedDict()

for _ in range(n):
    inp = input().split()
    item_name = ' '.join(inp[:len(inp)-1])
    item_price = inp[len(inp)-1]
    try:
        dictionary[item_name] += int(item_price)
    except:
        dictionary[item_name] = int(item_price)

for item in dictionary:
    print('{} {}'.format(item, dictionary[item]))