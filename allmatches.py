import re
string = input()
substring = input()
regex = re.compile('{}'.format(substring))
offset = 0
ctr = False
while(True):
    try:
        match = regex.search(string, offset)
        print('({}, {})'.format(match.start(), match.end()-1))
    except:
        break
    else:
        offset = offset + match.start()+1
        ctr = True

if not ctr:
    print('(-1, -1)')