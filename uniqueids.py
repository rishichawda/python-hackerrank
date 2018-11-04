import re
n = int(input())
for _ in range(n):
    uid = input()
    uel = len(re.findall(r'[A-Z]{2,}', uid)) > 0
    dig = len(re.findall(r'\d{3,}', uid))
    uc_len = bool(re.match(r'[A-Z\d]{10}', uid))
    rep = len(re.findall(r'(?=(.).*\1)', uid)) == 0
    print("Valid" if uid and dig and uc_len and rep else "Invalid")