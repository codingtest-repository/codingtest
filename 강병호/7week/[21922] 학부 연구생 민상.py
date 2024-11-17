'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.15(Fri)
* Runtime   : 4768 ms
* Memory    : 94708 KB
* Algorithm : 구현, 그래프 탐색
'''
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
def func(row):
    return row.count(True)
arr = []
aircon = deque()
visited = [[False for _ in range(M)] for _ in range(N)]
for x in range(N):
    temp = list(map(int,input().split()))
    for y in range(M):
        if temp[y] == 9:
            aircon.append((x,y,[0,1,2,3]))
            visited[x][y] = True
 
    arr.append(temp)
 
 
if aircon:
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    rotate_dict = {
        1 : [0,-1,2,-1],
        2 : [-1,1,-1,3],
        3 : [3,2,1,0],
        4 : [1,0,3,2]
    }
    # 북,서,남,동
    while aircon:
        x,y,dire = aircon.pop()
        for i in dire:
            nx = x + dx[i]
            ny = y + dy[i]
            while 0<=nx<N and 0<=ny<M :
                if arr[nx][ny] == 9:
                    break
                visited[nx][ny] = True
                if 0<=nx<N and 0<=ny<M and arr[nx][ny]:
                    if rotate_dict[arr[nx][ny]][i] != -1:
                        i = rotate_dict[arr[nx][ny]][i]
                    else:
                        break
                nx = nx + dx[i]
                ny = ny + dy[i]
 
    b = sum(list(map(func,visited)))
    print(b)
else:
    print(0)