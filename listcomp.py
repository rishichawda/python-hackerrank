if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = []

    def check(l):
        if sum(l) != n and l not in result:
            result.append(l)
        if l[0] < x:
            check([l[0]+1, l[1], l[2]])
        if l[1] < y:
            check([l[0], l[1]+1, l[2]])
        if l[2] < z:
            check([l[0], l[1], l[2]+1])
    
    check([0,0,0])
    
    print(sorted(result))
