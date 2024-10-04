"""
* Author    : SHIM SOMIN
* Date      : 2024.09.30 (Mon)
* Runtime   : 44 ms 
* Memory    : 33240 KB  
* Algorithm : 그리디
"""

import math

s = input()
cnt = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        cnt += 1

print(math.ceil(cnt/2))