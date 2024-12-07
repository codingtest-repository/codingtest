
'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.29(Fri)
* Runtime   : 540 ms
* Memory    : 32140 KB
* Algorithm : 구현, 시뮬레이션
'''
N, K = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split()))


def sol(S:int, D:list, K:list):
    N = len(S)
    for _ in range(K):
        original = [0] * N
        for i in range(N):
            original[D[i] - 1] = S[i]
        S = original
    return S

result = sol(S, D, K)

for i, num in enumerate(result):
    print(num, end='')
    if i < len(result) - 1:
        print(' ', end='')
print()