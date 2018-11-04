def count_substring(string, sub_string):
    temp = string
    counter = 0
    while len(temp) >= len(sub_string):
        index = temp.find(sub_string)
        if index != -1:
            counter += 1
        temp = temp[index+1:]
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)