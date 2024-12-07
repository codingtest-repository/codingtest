'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.29(Fri)
* Runtime   : 216 ms
* Memory    : 41388 KB
* Algorithm : 그래프, BFS, 최단 경로
'''
import heapq

N, K = map(int, input().split())


queue = [(0, N)]
visited = set()

def sol(N, K):

    while queue:
        time, pos = heapq.heappop(queue)
        
        if pos == K:
            return time
        
        if pos in visited:
            continue
        visited.add(pos)
        
        if pos * 2 <= 100000:
            heapq.heappush(queue, (time, pos * 2))
        if pos + 1 <= 100000:
            heapq.heappush(queue, (time + 1, pos + 1))
        if pos - 1 >= 0:
            heapq.heappush(queue, (time + 1, pos - 1))

print(sol(N, K))
