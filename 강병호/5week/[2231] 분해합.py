'''
* Author    : BYEONGHO KANG
* Date      : 2024.10.31(Thu)
* Runtime   : 1456 ms
* Memory    : 31120 KB
* Algorithm : Bruteforce
'''
N = int(input())
result = 0

for M in range(1, N):
    swift = M + sum(int(data) for data in str(M))
    if swift == N:
        result = M
        break

print(result)