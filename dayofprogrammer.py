#!/usr/local/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year > 1918:
        return ("12.9.{}").format(year) if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) else ("13.9.{}").format(year)
    elif year < 1918:
        return ("12.09.{}").format(year) if year % 4 == 0 else ("13.9.{}").format(year)
    else:
        return "26.9.1918"

if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)
    