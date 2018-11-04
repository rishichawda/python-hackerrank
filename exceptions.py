
for _ in range(int(input())):
    try:
        [a, b] = map(int, input().split())
        result = a // b
        print(result)
    except Exception as e:
        print('Error Code: {}'.format(e))
    finally:
        pass