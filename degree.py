# -*- coding: utf-8 -*-
import math

ab = float(input())
bc = float(input())

print(f'{int(round(math.degrees(math.atan2(ab,bc))))}\xb0')