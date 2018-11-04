n, m = map(int, input().split())
for i in range(int(n / 2)):
    print(('.|.'*((2*i)+1)).center(m, '-'))
print('WELCOME'.center(m, '-'))
for i in range(int(n / 2)+1, n):
    print(('.|.'*(((n - i)*2)-1)).center(m, '-'))
