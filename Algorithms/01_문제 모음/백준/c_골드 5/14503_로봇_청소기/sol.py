"""
문제 조건이 이해하기 애매한 부분이 있어 시간을 많이 소모함.
애매한 부분 (3번의 반시계 90도 방향 회전 로직)을 기록하기 위해 GPT를 통해 풀이를 기록.
"""

import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=====================================================================
# 방향에 맞는 델타 로직 (0:북 1:동 2:남 3:서)
dv = (-1, 0, 1, 0)
dh = (0, 1, 0, -1)

# 입력값 받기
N, M = map(int, sys.stdin.readline().split())
v, h, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 청소 로직 실행
cnt = 0
while True:

    # 1) 현재 칸이 청소되지 않은 칸이면 청소
    if not visited[v][h]:
        visited[v][h] = True
        cnt += 1

    # 3) 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우: 왼쪽 회전 4번 시도
    moved = False
    for _ in range(4):
        d = (d - 1) % 4  # 반시계(왼쪽) 회전
        nv = v + dv[d]
        nh = h + dh[d]

        if graph[nv][nh] == 0 and not visited[nv][nh]:
            v, h = nv, nh
            moved = True
            break

    if moved:
        continue

    # 2) 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우: 후진
    back = (d + 2) % 4
    bv = v + dv[back]
    bh = h + dh[back]

    if graph[bv][bh] == 0:
        v, h = bv, bh
    else:
        break

print(cnt)
#=====================================================================

e_t = time.time()
print("time: ", e_t - s_t)