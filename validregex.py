import re
n = int(input())

valid = True
for _ in range(n):
    try:
        re.compile(input())
    except:
        valid = False
    finally:
        print(valid)