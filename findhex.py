n = int(input())
list = []
for _ in range(n):
    list.append(input())
css = '\n'.join(list)
import re
matches = re.findall(r'(?<!^)(#(?:[\da-f]{3}){1,2})(?!\n)', css,re.I)
for match in matches:
    print(match)