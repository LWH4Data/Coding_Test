# - 칸 수에 출발 지점을 포함해야 한다.
# - index 설정 범위를 주의해야 한다.

import sys, time
sys.stdin = open("input.txt")
start = time.time()

#=============================================
from collections import deque
# 칸 수를 포함하여 상태관리. queue(x, y, cnt)

# 뎉타로직 (상, 하, 좌, 우)
dh = [0, 0, -1, 1]
dv = [-1, 1, 0, 0]

# BFS()
def BFS(x, y, cnt):
    queue = deque()
    queue.append((x, y, cnt))
    visited[x][y] # N, M

    while queue:
        # 값 받기
        x, y, cnt = queue.popleft()

        # 찾던 위치라면 종료
        if x == N-1 and y == M-1:
            return cnt

        # 이미 방문했다면 skip
        if visited[x][y]:
            continue
        
        # 아니라면 방문 표시
        visited[x][y] = True

        for i in range(4):
            nx = x + dv[i]
            ny = y + dh[i]
            
            # 범위 초과 예외 처리
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
        
            # 0인 경우 예외 처리
            if not graph[nx][ny]:
                continue 
            queue.append((nx, ny, cnt + 1))
    
    return cnt

# 입력값 받기
N, M = map(int, sys.stdin.readline().split())
# graph 구현 (N X M)
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
# 방문 
visited = [[False] * M for _ in range(N)]

# BFS 탐색
ans = BFS(0, 0, 0)
print(ans + 1)
#=============================================

end = time.time()
print("time:", start - end)