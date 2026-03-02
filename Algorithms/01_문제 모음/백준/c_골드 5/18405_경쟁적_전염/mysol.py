import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=============================================================
from collections import deque

# 델타 로직
dv = (-1, 1, 0, 0)
dh = (0, 0, -1, 1)

# < 함수: BFS로 외곽 좌표 찾기 >
def BFS(v, h):
    is_virus = graph[v][h]
    q = deque()
    q.append((v, h))
    visited = [[False] * N for _ in range(N)]
    visited[v][h] = True
    edge_virus = []

    while q:
        v, h = q.popleft()

        # 해당하는 바이러스가 아니면 탐색 필요 없음.
        is_same = False
        for i in range(4):
            nv, nh = v + dv[i], h + dh[i]
            
            # 범위 체크
            if nv < 0 or nv >= N or nh < 0 or nh >= N:
                continue

            # 방문하지 않았고
            if visited[nv][nh]:
                continue
            visited[nv][nh] = True

            # 확장 가능한 경우에면 append
            if graph[nv][nh] == 0:
                if not is_same:
                    # 현재 칸이 edge임.
                    edge_virus.append((v, h))
                    is_same = True
            
            # 탐색할 칸이 해당 바이러스가 아니면 탐색할 필요 없음.
            # print(graph[nv][nh], is_virus)
            if graph[nv][nh] != is_virus:
                continue

            # 아닌 경우 탐색
            q.append((nv, nh))
    
    return edge_virus

# < 함수: 바이러스 확산 >
def expand_virus(v, h):
    pass

# 입력
N, K = map(int, sys.stdin.readline().split()) # N: 시험관의 크기, K: 바이러스의 수
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 그래프
S, X, Y = map(int, sys.stdin.readline().split()) # S: 초, X: vertical, Y: horizontal

# 첫 바이러스의 위치를 기록.
#   - 외곽 위치를 리스트로 다룰 것이기에 이중 리스트 사용.
#   - idx는 0 ~ K
virus_position = [[] for _ in range(K + 1)]
for i in range(N):
    for j in range(N):
        if graph[i][j] !=0:
            virus_position[graph[i][j]].append((i, j))

# 바이러스 위치를 중심으로 외곽을 1회 기록.
print(len(virus_position[i]))
for i in range(1, len(virus_position) + 1):
    for j in range(len(virus_position[i])):
        virus_position[i] = BFS(virus_position[i][j][0], virus_position[i][j][1])
print(virus_position)

# S 초 동안 로직 수행.
check_S = 0
while check_S != S + 1: # S초 까지는 수행해야 함.
    break

    # 각 바이러스 1부터 바이러스 확산 로직을 수행한다.


# BFS로 가장 외곽의 칸만 모으기

# 외곽의 칸에서 바이러스 확장 로직 수행.

# 해당 위치 출력. (단, (0, 0)을 기준으로 하기에 -1을 해 주어야 함).
#=============================================================

e_t = time.time()
print("time: ", e_t - s_t)