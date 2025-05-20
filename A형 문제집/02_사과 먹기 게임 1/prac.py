import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#=============================================================
from collections import deque

dv = (0, 1, 0, -1)
dh = (1, 0, -1, 0)

def BFS(cur_v, cur_h, cur_d, target_v, target_h):
    visited = [[[False] * 4 for _ in range(N)] for _ in range(N)]
    visited[cur_v][cur_h][cur_d] = True
    queue =deque()
    queue.append((cur_v, cur_h, cur_d, 0))

    while queue:
        v, h, d, turn = queue.popleft()

        if (v, h) == (target_v, target_h):
            return (turn, v, h, d)
        
        nv = v + dv[d]
        nh = h + dh[d]

        if 0 <= nv < N and 0 <= nh < N and not visited[nv][nh][d]:
            visited[nv][nh][d] = True
            queue.append((nv, nh, d, turn))

        nd = (d + 1) % 4

        if not visited[v][h][nd]:
            visited[v][h][nd] = True
            queue.append((v, h, nd, turn + 1))

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    apples = []
    for v in range(N):
        for h in range(N):
            if graph[v][h] != 0:
                apples.append((graph[v][h], v, h))
    
    apples = sorted(apples)

    total_turns = 0
    cur_v, cur_h, cur_d = 0, 0, 0

    for _, target_v, target_h in apples:
        turns, cur_v, cur_h, cur_d = BFS(cur_v, cur_h, cur_d, target_v, target_h)
        total_turns += turns
    
    print(f'#{tc} {total_turns}')
#=============================================================

end_time = time.time()
print('time :', end_time - start_time)

# 6