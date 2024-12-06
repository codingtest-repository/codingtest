'''
* Author    : JUYEONG HA
* Date      : 2024.12.06(Fri)
* Runtime   : 180 ms 
* Memory    : 56452 KB
* Algorithm : Prefix Sum, Math
'''

import sys

input = sys.stdin.readline

n, L = map(int, input().split())
lst = list(map(int, input().split()))

def deter_is_stable(avg, x1, x2):
    if x1 < avg < x2:
        return True
    else:
        return False

is_stable = True
sum_above = sum(lst)

for i in range(n-1):
    sum_above -= lst[i]
    if not deter_is_stable(sum_above/(n-i-1), lst[i]-L, lst[i]+L):
        is_stable = False
        break

if is_stable:
    print("stable")
else:
    print("unstable")
    