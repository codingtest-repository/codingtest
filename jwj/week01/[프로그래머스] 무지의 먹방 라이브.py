'''
* Author    : Jang Woo Jin
* Date      : 2024.10.01(Tue)
* Runtime   : 305.96 ms
* Memory    : 39.3 MB
* Algorithm : priority queue
'''

# 우선순위 : 음식 번호
# 입력 조건을 분석해봤을때, 선형 탐색은 절대 불가능
# 선형 탐색 : O(N)
# 최소 힙 : O(N log N)
import heapq

def solution(food_times, k):
    heap = []
    for idx, food in enumerate(food_times):
        heapq.heappush(heap, (food, idx))
    
    if sum(food_times) <= k:
        return -1
    
    # 계산 부분
    # k초 이내의 범위에서는 무한 반복
    tt = 0  # 전체 시간
    nt = 0  # 현재 시간
    pt = 0  # 이전 시간
    length = len(heap)
    while tt + (heap[0][0] - pt) * length <= k:
        nt = heapq.heappop(heap)[0]
        tt += (nt - pt) * length
        length -= 1
        pt = nt 
        
    result = sorted(heap, key=lambda x : x[1])
    return result[(k - tt) % length][1] + 1