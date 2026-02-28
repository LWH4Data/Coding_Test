import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#========================================================================
from collections import deque

# 델타 로직
dv = (-1, 1, 0, 0)
dh = (0, 0, -1, 1)

# < 함수 >===============================================================
"""
BFS로 탐색하며 거리가 최소인 후보 물고기들을 탐색한다.
"""
def bfs_find_candidates(sv: int, sh: int, size: int):
    dist_map = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((sv, sh))
    dist_map[sv][sh] = 0

    candidates = []
    min_dist = None

    while q:
        v, h = q.popleft()
        cur_d = dist_map[v][h]

        # 이미 먹이를 찾은 경우 더 먼 거리의 먹이를 찾을 필요 없음.
        if min_dist is not None and cur_d > min_dist:
            # BFS는 거리 순서대로 찾기 때문에 넘어가는 순간 이전 거리의 탐색은 모두 끝난 것.
            break

        # 현재 칸이 먹을 수 있는 물고리라면 후보 추가.
        if 0 < graph[v][h] < size:
            if min_dist is None:
                min_dist = cur_d
            candidates.append((cur_d, v, h))
        
        for i in range(4):
            nv = v + dv[i]
            nh = h + dh[i]

            if nv < 0 or nv >= N or nh < 0 or nh >= N:
                continue
                
            # 큰 물고기는 지나갈 수 없음.
            if graph[nv][nh] > size:
                continue

            # 거리를 visited로 사용한다.
            if dist_map[nv][nh] != -1:
                continue
            dist_map[nv][nh] = cur_d + 1

            # 탐색 추가.
            q.append((nv, nh))

    return candidates

# 풀이====================================================================
# 입력
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 상어 위치 찾기.
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            sv, sh  = i, j
            graph[i][j] = 0

# 상어의 상태 정보
size = 2
eat = 0
total_dist = 0

# 탐색 시작.
while True:
    candidates = bfs_find_candidates(sv, sh, size)

    # 먹을 수 있는 물고기가 없다면 종료.
    if not candidates:
        break

    # (거리, 행, 열) 기준 정렬 -> 첫 번째가 규칙에 맞는 먹이.
    candidates.sort()
    dist, fv, fh = candidates[0]

    # 상어 이동 + 누적거리 업데이트
    sv, sh = fv, fh
    total_dist += dist

    # 물고기 먹기.
    graph[sv][sh] = 0
    eat += 1

    # 크기 증가 확인.
    if eat == size:
        size += 1
        eat = 0

print(total_dist)
#========================================================================

e_t = time.time()
print("time: ", e_t - s_t)