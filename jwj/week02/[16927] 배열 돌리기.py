'''
* Author    : Jang Woo Jin
* Date      : 2024.10.07(Mon)
* Runtime   : 288 ms
* Memory    : 111880 KB (PyPy3)
* Algorithm : implementation
'''

import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

# 내/외부 회전 수 규칙 파악(다시 원래대로 돌아오기까지)
turn_cnt = []
for i in range(min(N, M) // 2):
    turn_cnt.append(2 * ((N - 2 * i) + (M - 2 * i)) - 4)
    
# 반시계 방향 회전
# 전체를 돌리는 것이 아닌 N, M 최솟값 중 절반 범위까지만
for i in range(min(N, M) // 2):
    for j in range(R % turn_cnt[i]):
        first = array[i][i]

        # 위쪽 변
        for k in range(i+1, M-i):
            array[i][k-1] = array[i][k]
        
        # 오른쪽 변
        for k in range(i+1, N-i):
            array[k-1][M-1-i] = array[k][M-1-i]
        
        # 아래쪽 변
        for k in range(i+1, M-i):
            array[N-1-i][M-k] = array[N-1-i][M-1-k]
             
        # 왼쪽 변
        for k in range(i+1, N-i):
            array[N-k][i] = array[N-1-k][i]     
        
        # 맨 처음 빼놨던 값을 회전 마지막 결과에 포함시켜야 함
        array[i+1][i] = first
            
for row in array:
    print(*row)