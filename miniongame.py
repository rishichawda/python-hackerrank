s = str(input())
vowels = 'AEIOU'

# def overlapping_count(substring, string):
#     import re
#     regex = re.compile('(?={0})'.format(substring))
#     return len(re.findall(regex, string))

kevin = 0
stuart = 0
checked = []
kevin_words = []
# for index in range(len(s)):
#     substring = s[index:]
#     for n in range(index + 1, len(s) + 1):
#         subs = s[index:n]
#         if subs not in checked:
#             checked.append(subs)
#             if subs[0].upper() not in vowels:
#                 stuart += overlapping_count(subs, s)
#             else:
#                 kevin += overlapping_count(subs, s)

for i in range(len(s)):
    if s[i] in vowels:
        kevin += (len(s)-i)
    else:
        stuart += (len(s)-i)

if kevin > stuart:
    print("Kevin", kevin) 
elif kevin < stuart:
    print("Stuart", stuart)
else:
    print("Draw")