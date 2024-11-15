
# 런타임 에러 해결 필요
N, K, Q, M = map(int, input().split())

sleeping_students = set(map(int, input().split()))
attendance_students = set(map(int, input().split()))

status = [True] * (N + 1)

for student in sleeping_students:
    if 1 <= student <= N:
        status[student] = False

for student in attendance_students:
    if 1 <= student <= N and not status[student]:
        status[student] = True

absent_count = [0] * (N + 2)
for i in range(1, N + 1):
    absent_count[i] = absent_count[i - 1] + (1 if not status[i] else 0)

for _ in range(M):
    S, E = map(int, input().split())
    print(absent_count[E] - absent_count[S - 1])