'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.14(Thu)
* Runtime   : 72 ms
* Memory    : 31120 KB
* Algorithm : 백트래킹
'''

N, K = map(int, input().split())
arr = list(map(int, input().split()))
chk = [False] * N 

result = 0

def backtracking(current_weight, cnt):
    global result
    if cnt == N:
        result += 1
        return

    for i in range(N):
        if not chk[i]:
            next_weight = current_weight + arr[i] - K 
            if next_weight >= 500:
                chk[i] = True
                backtracking(next_weight, cnt + 1)
                chk[i] = False

backtracking(500, 0)
print(result)