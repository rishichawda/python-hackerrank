from email.utils import parseaddr, formataddr
import re
for _ in range(int(input())):
    t = parseaddr(input())
    if bool(re.match(r'[a-zA-Z](\w|-|\.)*@[a-zA-Z]+\.[a-zA-Z]{0,3}$',t[1])):
        print(formataddr(t))