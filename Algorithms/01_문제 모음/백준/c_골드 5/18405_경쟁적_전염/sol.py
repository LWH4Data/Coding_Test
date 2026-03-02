import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=============================================================
from collections import deque

# 델타 로직
dv = (-1, 1, 0, 0)
dh = (0, 0, -1, 1)

# < 함수: 바이러스 확산 시뮬레이션 >
def simulate():
    # 초기 바이러스 정보 저장.
    # (바이러스 번호, 시간, v, h)
    viruses = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                viruses.append((graph[i][j], 0, i, j))
    
    # 같은 시간대에 확산될 때 번호 작은 바이러스 먼저 처리되도록 정렬.
    viruses.sort()

    # BFS 탐색
    q = deque(viruses)

    while q:
        virus_id, t, v, h = q.popleft()

        # S초가 되면 종료.
        if t == S:
            break
        
        # 델타 탐색
        for d in range(4):
            nv, nh = v + dv[d], h + dh[d]
            
            # 범위 초과시 skip
            if nv < 0 or nv >= N or nh < 0 or nh >= N:
                continue

            # 아닌 경우 graph 업데이트
            graph[nv][nh] = virus_id
            q.append((virus_id, t + 1, nv, nh))

# 입력
N, K = map(int, sys.stdin.readline().split()) # N: 시험관 크기, K: 바이러스 종류
graph =  [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, sys.stdin.readline().split()) # S: 초, X, vertical, Y: horizontal

simulate()

# 정답 출력. ((0, 0) 좌표를 사용했기에 -1을 해야 함).
print(graph[X - 1][Y - 1])
#=============================================================

e_t = time.time()
print("time: ", e_t - s_t)