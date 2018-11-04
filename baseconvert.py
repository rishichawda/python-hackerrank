n = int(input())
decimal = []
octal = []
hexa = []
binary = []
for i in range(1, n + 1):
    decimal.append(i)
    octal.append(oct(i)[2:])
    hexa.append((hex(i)[2:]).upper())
    binary.append(bin(i)[2:])

padding = len(str(binary[len(binary) - 1]))
for i in range(n):
    print((str(decimal[i]).rjust(padding, ' ')) + ' ' + (str(octal[i]).rjust(padding, ' ')) + ' ' + (str(hexa[i]).rjust(padding, ' ')) + ' ' + (str(binary[i]).rjust(padding, ' ')))