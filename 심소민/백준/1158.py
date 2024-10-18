'''
* Author    : SHIM SOMIN
* Date      : 2024.10.17(Thur)
* Runtime   : 36 ms
* Memory    : 31120 KB
* Algorithm : 구현
'''

N, K = map(int, input().split())
people = list(range(1, N + 1))
result = []
index = 0

while people:
    index = (index + K - 1) % len(people)
    result.append(people.pop(index))

print("<" + ", ".join(map(str, result)) + ">")