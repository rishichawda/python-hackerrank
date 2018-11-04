import re
string = input()
matches = re.findall(r'([a-zA-Z0-9])\1+', string)
if len(matches) > 0:
    print(matches[0])
else:
    print(-1)