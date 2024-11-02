'''
* Author    : BYEONGHO KANG
* Date      : 2024.11.1(Fri)
* Runtime   : 56 ms
* Memory    : 34068 KB
* Algorithm : Graph, BFS, DFS
'''

from collections import deque

coms = int(input())

# 딕셔너리 컴프리헨션 사용
com = {i: [] for i in range(1, coms + 1)}
check = [False] * (coms + 1)

connec = int(input())

for _ in range(connec):
    a, b = map(int, input().split())
    com[a].append(b)
    com[b].append(a)

che = deque()
check[1] = True

for elem in com[1]:
    che.append(elem)
    check[elem] = True

while che:
    num = che.popleft()
    for elem in com[num]:
        if not check[elem]:
            che.append(elem)
            check[elem] = True

count = sum(1 for i in range(2, coms + 1) if check[i])

print(count)