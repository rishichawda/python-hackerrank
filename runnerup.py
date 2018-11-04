#!/usr/local/bin/python3

if __name__ == "__main__":
  list = [29,2,11,16,20,25,25];
  unique = []
  for num in list:
    if num not in unique:
      unique.append(num)
  list = sorted(unique)
  runnerup = list[len(list) - 2]
  print(runnerup)
