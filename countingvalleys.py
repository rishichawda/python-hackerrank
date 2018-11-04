#!/usr/local/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    valley = 0
    for i in s:
        level = level + 1 if i == 'U' else level - 1
        valley = valley + 1 if level == 0 and i == 'U' else valley
    return valley

if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)