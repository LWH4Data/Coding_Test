import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#========================================================================
from collections import deque

# 나이트의 이동 로직
dv = (-2, -1, 1, 2, 2, 1, -1, -2)
dh = (1, 2, 2, 1, -1, -2, -2, -1)

# 입력
T = int(sys.stdin.readline())

for _ in range(T):

    # 입력 (한 변의 길이).
    N = int(sys.stdin.readline())
    v, h = map(int, sys.stdin.readline().split())
    tv, th = map(int, sys.stdin.readline().split())

    # 탐색 준비 (거리 문제이기에 visited는 거리)
    graph = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((v, h))
    graph[v][h] = 0

    while q:
        v, h = q.popleft()

        # 찾는 위치면 중지
        if v == tv and h == th:
            print(graph[v][h])
            break

        # 아닌 경우 탐색.
        for i in range(8):
            nv = v + dv[i]
            nh = h + dh[i]

            # 범위 넘으면 skip
            if nv < 0 or nv >= N or nh < 0 or nh >= N:
                continue
            
            # 만약 방문 했다면 skip
            if graph[nv][nh] != -1:
                continue

            # 아닌 경우 거리 업데이트
            graph[nv][nh] = graph[v][h] + 1

            # q에 추가.
            q.append((nv, nh))
#========================================================================

e_t = time.time()
print("time: ", e_t - s_t)