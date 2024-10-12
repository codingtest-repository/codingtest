'''
* Author    : Yooyoung Lee
* Date      : 2024.10.12(Sat)
* Runtime   : 2604 ms
* Memory    : 31836 KB
* Algorithm : Implementation
'''
import sys

input = sys.stdin.readline

from itertools import product
from copy import deepcopy

# 상수 선언
UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)

# 입력 받기
n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]


def color_map(x, y, tmp_map, d_info):
    for dx, dy in d_info:
        cx, cy = x, y  # 기준점
        while 0 <= cx + dx < n and 0 <= cy + dy < m and tmp_map[cx+dx][cy+dy] != 6:
            if tmp_map[cx+dx][cy+dy] == '#' or 1 <= tmp_map[cx+dx][cy+dy] <= 5:  # jump
                cx += dx
                cy += dy
                continue
            tmp_map[cx+dx][cy+dy] = '#'
            cx += dx
            cy += dy


def count_zeros(tmp_map):
    total_cnt = 0
    for i in range(len(tmp_map)):
        for j in range(len(tmp_map[i])):
            if tmp_map[i][j] == 0:
                total_cnt += 1
    return total_cnt


# 위치 정보와 번호 정보 찾아서 저장
infos = []
for i in range(n):
    for j in range(m):
        if 1 <= office[i][j] <= 5:
            infos.append([office[i][j], i, j])  # [번호, x, y]

# CCTV 방향 정보
num_one = [[RIGHT], [DOWN], [LEFT], [UP]]
num_two = [[LEFT, RIGHT], [UP, DOWN]]
num_three = [[UP, RIGHT], [RIGHT, DOWN], [DOWN, LEFT], [LEFT, UP]]
num_four = [[LEFT, UP, RIGHT], [UP, RIGHT, DOWN], [RIGHT, DOWN, LEFT], [DOWN, LEFT, UP]]
num_five = [[UP, RIGHT, DOWN, LEFT]]

dirs = []  # infos에 맞게 해당되는 방향 정보 저장
for num, x, y in infos:
    if num == 1:
        dirs.append(num_one)
    elif num == 2:
        dirs.append(num_two)
    elif num == 3:
        dirs.append(num_three)
    elif num == 4:
        dirs.append(num_four)
    elif num == 5:
        dirs.append(num_five)


# 해당 영역에 맞게 색칠하는 모든 경우의 수 -> 가장 많이 색칠된 영역으로 갱신
area_cnt = float('inf')
for d_infos in product(*dirs):
    tmp_map = deepcopy(office)
    for info, d_info in zip(infos, d_infos):
        color_map(info[1], info[2], tmp_map, d_info)
    area_cnt = min(count_zeros(tmp_map), area_cnt)


print(area_cnt)