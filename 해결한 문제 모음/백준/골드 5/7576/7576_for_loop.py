import sys
from collections import deque

sys.stdin = open('input_7576.txt')

T = int(input())
for tc in range(1, T + 1):
    M, N = map(int, input().split())  # M: 가로 / N: 세로
    board = [list(map(int, input().split())) for _ in range(N)]

    queue = deque()

    # 델타 탐색 (좌, 우, 상, 하)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 익은 토마토 위치를 큐에 삽입
    for n in range(N):
        for m in range(M):
            if board[n][m] == 1:
                queue.append((n, m))

    ans = -1  # 첫날 0일을 맞추기 위해 -1로 설정

    while queue:
        ans += 1
        '''
        ** 뭐지 for loop과 len()을 활용 했었는데 안 됐었는데;; **
        '''
        for _ in range(len(queue)):  # 하루치 탐색을 진행
            x, y = queue.popleft()

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]

                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                    board[nx][ny] = 1
                    queue.append((nx, ny))

    # 모든 탐색 후 0이 남아있는지 체크
    for row in board:
        if 0 in row:
            ans = -1
            break

    print(ans)
