import re
P = input()

regex_integer_in_range = r"^[1-9]{1}[0-9]{5}"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=.*((\d)\d\2).*)"	# Do not delete 'r'.

print(re.findall(regex_alternating_repetitive_digit_pair, P))
print(len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)