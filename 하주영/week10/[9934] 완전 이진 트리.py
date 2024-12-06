'''
* Author    : JUYEONG HA
* Date      : 2024.12.02(Mon)
* Runtime   : 32 ms
* Memory    : 31120 KB
* Algorithm : tree, recursive
'''

k = int(input())
arr = list(map(int, input().split()))

steps = [ [] for _ in range(k+1)]

def solution(arr, step):
    if len(arr) == 1:
        steps[step].append(arr[0])
        return
    
    # 중간 값 찾기
    mid_index = len(arr) // 2
    steps[step].append(arr[mid_index])

    solution(arr[:mid_index], step + 1) # 왼쪽 자식 트리
    solution(arr[mid_index+1:], step + 1) # 오른쪽 자식 트리

solution(arr, 1)

for arr in steps[1:]:
    for i in arr:
        print(i, end=' ')
    print()


