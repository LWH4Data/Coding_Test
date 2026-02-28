import sys
from collections import deque

# 델타 로직 (상, 하, 좌, 우)
dv = [-1, 1, 0, 0]
dh = [0, 0, -1, 1]

def bfs_find_candidates(sv: int, sh: int, size: int):
    """
    sv, sh: 상어 현재 위치
    size: 상어 크기
    return: 먹을 수 있는 물고기 후보 리스트 [(dist, v, h), ...]  (dist 최소인 것들만)
            후보가 없으면 []
    """
    # 거리를 visited로 사용한다.
    dist_map = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((sv, sh))
    dist_map[sv][sh] = 0

    candidates = []
    min_dist = None  # 발견한 최단 먹이 거리

    while q:
        v, h = q.popleft()
        cur_d = dist_map[v][h]

        # 이미 최단거리 먹이를 찾았는데, 그보다 멀리 가는 탐색은 의미 없음
        if min_dist is not None and cur_d > min_dist:
            break

        # 현재 칸이 "먹을 수 있는 물고기"면 후보에 추가
        if 0 < graph[v][h] < size:
            if min_dist is None:
                min_dist = cur_d
            candidates.append((cur_d, v, h))
            # 같은 거리의 다른 후보도 찾아야 하므로 continue는 하지 않음
            # (다만 cur_d == min_dist인 레벨까지만 진행됨)

        for i in range(4):
            nv = v + dv[i]
            nh = h + dh[i]

            if nv < 0 or nv >= N or nh < 0 or nh >= N:
                continue

            # 상어보다 큰 물고기는 지나갈 수 없음
            if graph[nv][nh] > size:
                continue
            
            # 거리를 visited로 사용한다.
            if dist_map[nv][nh] != -1:
                continue
            dist_map[nv][nh] = cur_d + 1

            q.append((nv, nh))

    return candidates


# 입력
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 상어 위치 찾기
sv = sh = -1
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            sv, sh = i, j
            graph[i][j] = 0  # 시작 위치는 빈칸 처리

# 상어 상태
size = 2
eaten = 0
total_dist = 0

while True:
    candidates = bfs_find_candidates(sv, sh, size)

    # 먹을 수 있는 물고기 없음 -> 종료
    if not candidates:
        break

    # (거리, 행, 열) 기준 정렬 -> 첫 번째가 규칙에 맞는 먹이
    candidates.sort()
    dist, fv, fh = candidates[0]

    # 이동 + 누적 거리
    sv, sh = fv, fh
    total_dist += dist

    # 물고기 먹기
    graph[sv][sh] = 0
    eaten += 1

    # 크기 증가 조건
    if eaten == size:
        size += 1
        eaten = 0

print(total_dist)