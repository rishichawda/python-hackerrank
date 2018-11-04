n = int(input()) # let n = 5
for i in range(n): # 0 to 4
    alphabets = []
    for num in range(i+1):
        alphabets.append(chr((n - num) + 96))
    for num in range(i-1, -1, -1):
        alphabets.append(chr( (n - num) + 96 ))
    print('-'.join(alphabets).center((4 * (n - 1) + 1), '-'))
for i in range(n - 1):
    alphabets = []
    for num in range(n - (i+1)):
        alphabets.append(chr((n-num)+96))
    for num in range(n - (i+3), -1, -1):
        alphabets.append(chr((n-num)+96))
    print('-'.join(alphabets).center((4 * (n - 1) + 1), '-'))