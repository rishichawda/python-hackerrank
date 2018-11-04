#!/usr/local/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    _unique = []
    _paired = []
    _result = 0
    for sock in ar:
        if sock not in _unique:
          _unique.append(sock)
          _paired.append(True)
        _paired[_unique.index(sock)] = not _paired[_unique.index(sock)]
        _result = _result + 1 if _paired[_unique.index(sock)] == True else _result
    return _result

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)