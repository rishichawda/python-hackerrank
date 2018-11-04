s = input()
alphanum = False
alpha = False
numeric = False
locase = False
upcase = False

for c in s:
    if c.isalpha() and not alpha:
        alpha = True
    if c.isalnum() and not alphanum:
        alphanum = True
    if c.isdigit() and not numeric:
        numeric = True
    if c.islower() and not locase:
        locase = True
    if c.isupper() and not upcase:
        upcase = True
    if alpha and alphanum and numeric and locase and upcase:
        break
print(alphanum)
print(alpha)
print(numeric)
print(locase)
print(upcase)