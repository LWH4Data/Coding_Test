import sys
sys.stdin = open('input_14502.txt')

from collections import deque

def dfs(i, j, cnt):
    global max_val

    if i < 0 or i >= N or j < 0 or j >= M:
        return

    # 3인 경우, 즉 모든 벽을 다 세운 경우 
    # BFS를 수행한 뒤, 남은 0의 수를 모두 체크한다.
    # 그리고 0의 수를 max_val에 전달.
    if cnt == 3:
        queue = deque()
        for i in range(N):
            for j in range(M):
                if board[i][j] == 2:
                    queue.append((i, j)) # [(세균1 x, 세균1 y), [세균2 x, 세균2 y], ...]
        total_sum = 0
        
        # 델타 탐색 로직
        dx = (-1, 1, 0, 0) # 상, 하, 좌, 우
        dy = (0, 0, -1, 1) # 상, 하, 좌, 우
        visited2 = [[False] * M for _ in range(N)]

        while queue:
            start = queue.popleft()
            visited2[start[0]][start[1]] = True

            for k in range(4):
                nx = start[0] + dx[k]
                ny = start[1] + dy[k]
                visited2[nx][ny] = True

                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 2 and not visited:
                    queue.append((nx, ny))
            
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    total_sum += 1

        max_val = max(max_val, total_sum)
        
    if board[i][j] == 0 and not visited:
        visitied = True
        board[i][j] = 1
    
    dfs(i - 1, j, cnt + 1) # 상
    dfs(i + 1, j, cnt + 1) # 하
    dfs(i, j - 1, cnt + 1) # 좌
    dfs(i, j + 1, cnt + 1) # 우


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N은 세로 / M은 가로
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    max_val = 0

    dfs(0, 0, 1)


    break




'''
1. 세로 N / 가로 M

2. 바이러스가 있는 칸은 상하좌우로 인접한 모든 빈 칸으로 퍼져나갈 수 있다. -> 델타 탐색 + BFS

3. 세울 수 있는 벽의 수는 꼭 3 개
    - DFS 완탐?
'''

'''
< 로직 >
1. DFS로 벽을 세우는 경우의 수를 처리하고,

2. 각 경우의 수마다 BFS로 안전지대(0)의 수를 찾아야 할 듯.
    - 총 0의 수를 max로 다음으로 전달하면서 모든 탐색이 끝나면 반환.
'''