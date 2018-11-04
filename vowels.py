import re
matches = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])[aeiou]{2,}(?=[qwrtypsdfghjklzxcvbnm])', input(), re.I)
if len(matches) > 0:
    for i in matches:
        print(i)
else:
    print(-1)
