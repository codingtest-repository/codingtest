import sys, copy
input = sys.stdin.readline

# 최악의 경우 계산
# 전체 지도 크기 : 64
# CCTV 최대 개수 : 8개

# 따라서 모든 경우를 고려한 순열/조합 라이브러리로는 절대 해결 불가능

modes = [
    [],                                           # 0번
    [(0, ), (1, ), (2, ), (3, )],                 # 1번
    [(1, 3), (0, 2)],                             # 2번
    [(0, 1), (1, 2), (2, 3), (3, 0)],             # 3번
    [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]], # 4번
    [[0, 1, 2, 3]],                               # 5번  
]

# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

result = float('inf') # 사각지대 최소 영역 크기
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# cctv 위치 정보 및 번호 저장
cctvs = []
for i in range(N):
    for j in range(M):
        if board[i][j] not in [0, 6]:
            cctvs.append([i, j, board[i][j]])

# cctv마다 탐색할 수 있는 범위가 따로 있으므로
def search(maps, mode, y, x):
    for i in mode:
        ny = y
        nx = x
        while True:
            ny += dy[i]
            nx += dx[i]
                
            # 영역을 벗어나는 경우
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                break
            
            # 영역 안에 있는 경우
            if 0 <= ny < N and 0 <= nx < M:
                # 벽이면 중단
                if maps[ny][nx] == 6:
                    break
                # 빈 칸이면 cctv 체크 가능 영역
                if maps[ny][nx] == 0:
                    maps[ny][nx] = -1

def process(depth, maps):
    global result
    # 현재 주어진 지도 정보에서 CCTV 개수만큼 다 돌렸다면(종료)
    if depth == len(cctvs):
        cnt = 0
        for row in maps:
            cnt += row.count(0)
        result = min(result, cnt)
        return
    
    cb = copy.deepcopy(maps)
    y, x, cn = cctvs[depth]
    # CCTV 번호별 탐색 가능 방향만큼
    for mode in modes[cn]:
        search(cb, mode, y, x)
        process(depth+1, cb)
        cb = copy.deepcopy(maps)

process(0, board)
print(result)