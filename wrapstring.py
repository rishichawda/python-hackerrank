s = str(input())
n = int(input())
temp = []
while len(s) > 0:
    temp.append(s[:n])
    s = s[n:]
print('\n'.join(temp))