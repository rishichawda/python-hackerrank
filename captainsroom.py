from collections import Counter
input()
rooms = Counter(input().split())
[captain] = [key for key in rooms if rooms[key] == 1]
print(captain)
