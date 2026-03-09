import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#============================================================================
from collections import deque

# 델타
dv = (-1, 1, 0, 0)
dh = (0, 0, -1, 1)

# < 함수: BFS로 탐색하며 정보를 업데이트 한다 >
def BFS(v, h):
    q = deque()
    q.append((v, h))
    visited[v][h] = True
    size = 1 # 자기 자신도 섬의 크기로 포함.

    while q:
        v, h = q.popleft()

        for i in range(4):
            nv = v + dv[i]
            nh = h + dh[i]

            # 범위 확인
            if nv < 0 or nv >= n or nh < 0 or nh >= m:
                continue
            
            # 1인 경우만 탐색하게 하여 영역의 크기를 확인한다.
            if not visited[nv][nh] and graph[nv][nh] == 1:
                visited[nv][nh] = True
                size += 1
                q.append((nv, nh))

    sum_list.append(size)

# 입력
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
sum_list = []

# 1이면서 방문 안한 모든 칸에서 BFS를 수행.
for v in range(n):
    for h in range(m):
        if graph[v][h] == 1 and not visited[v][h]:
            BFS(v, h)

# 정답 출력
if len(sum_list) == 0:
    print(0)
else:
    print(len(sum_list))

if len(sum_list) == 0:
    print(0)
else:
    print(max(sum_list))
#============================================================================

e_t = time.time()
print("time: ", e_t - s_t)