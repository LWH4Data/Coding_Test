import sys
sys.stdin = open('input_7576.txt')

from collections import deque

T = int(input())
for tc in range(1, T + 1):
    M, N = map(int, input().split()) # M : 가로 / N : 세로
    board = [list(map(int, input().split())) for _ in range(N)] # 세로의 수만큼 받아와야 하니 N

    queue = deque()

    # 델타 탐색 구현
    dx = (0, 0, -1, 1) # 좌 우 상 하 / 세로 축
    dy = (-1, 1, 0, 0) # 좌 우 상 하 / 가로 축

    for m in range(M):
        for n in range(N):
            if board[n][m] == 1:
                queue.append((n, m))

    # 정답을 받을 변수 초기화
    ans = -1 # while 문을 
    day = []

    # BFS 수행
    '''
    1. '일' 단위로 연산이 수행되어야 하는 슬픈 이야기가 있음.
    2. 이를 구현하기 위해서 다음과 같은 로직을 생각함
        -> 현재 큐를 다 돌면 1일 이다.
        -> 그럼 현재 큐가 순회되는 동안 다음 순회할 항목들을 저장할 리스트가 필요하다. (day = [] 활용)
        -> 현재 큐를 다 순회하였다면 큐를 다음 순회 항목(day)으로 초기화한다.
        -> 이후 다시 day = []로 하여 다음 탐색 범위를 받을 준비를 한다.
    3. 문제의 경우 'n 일 후'이기 때문에 첫 번째 토마토 증식은 포함되지 않은다(0일 임).
        -> 따라서 'line 23'과 같이 시작부터 '-1'을 할당하여 날짜를 맞추어 준다.
    '''
    while queue:
        ans += 1 
        for toma in queue: # 
            for k in range(4):
                nx = toma[0] + dx[k] 
                ny = toma[1] + dy[k]

                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                    continue

                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == -1:
                    continue

                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                    board[nx][ny] = 1 # visited를 하지 않아도 직접 값을 변화 시키기에 괜찮다.
                    day.append((nx, ny))
        
        queue = day
        day = []

    # 전체 탐색을 했음에도 0이 남아있다면
    # 탐색이 불가하기에 '-1'을 출력하도록 한다.
    for n in range(N):
        for m in range(M):
            if board[n][m] == 0: 
                ans = -1

    # 모든 토마토가 익은 경우는 while문에 포함되기에 작성하지 않는다.
    print(ans)                

'''
1. M : 가로, N : 세로
    - 최대 1000 x 1000 = 1000,000으로 완탐가능.

2. 토마토 기준
    - 1 : 익은 토마토
    - 0 : 익지 않은 토마도
    - -1 : 토마토 없음.

3. 로직
    3-1. 토마토가 있는 셀을 탐색한다.
    3-2. 해당 셀을 큐에 넣고 탐색을 시작한다.
        - 탐색 방법은 델타 탐색
    3-3. 탐색 후 해당 영역이 익지 않은 토마토라면 큐에 append하여 탐색을 진행한다.
    3-4. 탐색 완료 시 종료
'''