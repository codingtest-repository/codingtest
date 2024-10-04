'''
* Author    : Yooyoung Lee
* Date      : 2024.10.02(Wed)
* Runtime   : 32 ms
* Memory    : 31120 KB
* Algorithm : Greedy
'''
import sys
input = sys.stdin.readline


def solution(num):
    # 뒤집지 않아도 되는 경우
    if len(set(num)) == 1:
        return 0

    length = len(num)
    cnt = [0] * 2  # 연속된 O/1 뭉텅이 개수
    for i in range(1, length):
        cur, nxt = int(num[i - 1]), int(num[i])
        if cur != nxt:
            cnt[cur] += 1
        if i == length - 1:  # 끝 처리
            cnt[nxt] += 1

    return min(cnt)


print(solution(input().rstrip()))
