'''
* Author    : BYEONGHO KANG
* Date      : 2024.10.31(Thu)
* Runtime   : 112 ms
* Memory    : 31120 KB
* Algorithm : Bruteforce
'''

N, K = map(int, input().split())
count = 0

for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            if str(K) in f"{h:02}{m:02}{s:02}":
                count += 1

print(count)