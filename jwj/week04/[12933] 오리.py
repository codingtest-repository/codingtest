'''
* Author    : Jang Woo Jin
* Date      : 2024.10.25(Fri)
* Runtime   : 84 ms
* Memory    : 31120 KB
* Algorithm : implementation
'''


import sys
input = sys.stdin.readline

sound = input().strip()
visited = [False] * len(sound)
lst = ['q', 'u', 'a', 'c', 'k']

result = 0
length = len(sound)

for i in range(length):
    if visited[i]:
        continue
    
    idx = 0
    flag = False
    for j in range(i, length):
        if visited[j]:
            continue
        if lst[idx] == sound[j]:
            visited[j] = True
            idx += 1
            if idx == 5:
                flag = True
                idx = 0
    
    if flag:
        result += 1
    
    # 반례 : qucack -> c는 울음 소리에 해당하지 않기 때문에 방문 여부가 체크가 안됨
    # 따라서 울다 만 경우하고 현재 인덱스를 방문하지 않은 경우 -1로 처리
    if idx > 0 or not visited[i]:
        print(-1)
        sys.exit(0)

print(result)