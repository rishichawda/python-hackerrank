#!/usr/local/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def _kangaroo(x1, v1, x2, v2):
    steps = 0
    try:
      steps = (x2 - x1)/(v1 - v2)
    except ZeroDivisionError:
      return "NO"
    finally:
      return "YES" if (steps > 0 and round(steps) == steps ) else "NO"


if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = _kangaroo(x1, v1, x2, v2)

    print(result)
