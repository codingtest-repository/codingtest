'''
* Author    : JUYEONG HA
* Date      : 2024.11.29(Fri)
* Runtime   : 132 ms
* Memory    : 34652 KB
* Algorithm : BFS
'''

import sys
from collections import deque

input = sys.stdin.readline

MAX_PATH_LENGTH = 100001 # 일직선 상의 최대 좌표
start, finish = map(int,input().split()) # 출발, 도착
visited = [False] * MAX_PATH_LENGTH # 방문 표시를 저장할 배열

q = deque() 
q.append((start, 0))
visited[start] = True

def isRange(x):
    return 0 <= x < MAX_PATH_LENGTH

while q: # bfs
    cur_loc, cur_cnt = q.popleft()
    
    if cur_loc == finish: # 도착했다면 반복문 탈출
        print(cur_cnt) 
        break

    for next_loc in (cur_loc*2, cur_loc-1, cur_loc+1):
        if isRange(next_loc) and not visited[next_loc]:
            if next_loc == cur_loc*2:
                q.append((next_loc, cur_cnt)) # 순간이동은 0초 동안 이루어진다
            else:
                q.append((next_loc, cur_cnt +1)) # 좌우이동은 1초 동안 이루어진다
            visited[next_loc] = True

