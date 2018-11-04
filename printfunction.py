if __name__ == '__main__':
    n = int(input())
    res = 0
    digits = 10
    for i in range(n+1):
        if i/digits >= 1:
            digits *= 10
        res = (res * digits) + i
    print(res)