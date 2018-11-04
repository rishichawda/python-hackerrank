#!/usr/local/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if n == p:
        return 0
    return p // 2 if p <= n//2 else (n - p)//2+1 if (n - p)//2 == 0 and n % 2 == 0 else (n - p)//2

if __name__ == '__main__':

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(result)

