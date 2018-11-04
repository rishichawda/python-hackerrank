import re
for _ in range(int(input())):
    print("YES" if bool(re.match(r'^[789]{1}[\d]{9}$', input())) else "NO")