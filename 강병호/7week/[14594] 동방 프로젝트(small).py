'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.8(Fri)
* Runtime   : 36 ms
* Memory    : 31120 KB
* Algorithm : 구현, 시뮬레이션
'''
N = int(input())
M = int(input())
walls = [True] * (N - 1)

for _ in range(M):
    x, y = map(int, input().split())
    for i in range(x - 1, y - 1): 
        walls[i] = False


room_count = 1 
for i in range(N - 1):
    if walls[i]:
        room_count += 1

print(room_count)