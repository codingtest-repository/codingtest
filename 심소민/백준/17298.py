'''
* Author    : SHIM SOMIN
* Date      : 2024.10.18(Fri)
* Runtime   : 868 ms
* Memory    : 202408 KB
* Algorithm : 스택
'''

n = int(input())
arr = list(map(int, input().split()))
ans = [-1] * n  # 오큰수를 저장할 리스트, 초기값 -1
stack = []

for i in range(n):
    # 스택이 비어있지 않고, 현재 원소가 스택의 top 보다 클 때
    while stack and arr[stack[-1]] < arr[i]:
        index = stack.pop()
        ans[index] = arr[i]
    stack.append(i)

print(*ans)