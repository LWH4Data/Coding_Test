import sys
sys.stdin = open('input_14502.txt')

from collections import deque

# BFS로 바이러스 확산
def spread_virus():
    '''
    < 여기서 왜 copy 함? visited 쓰면 안됨? >
    1. BFS 함수를 DFS 내에서 반복 호출하기 때문에
        -> 이 때마다 visited를 하게 되면 연산이 늘어남.
    2. 따라서 visited를 하지않고 새로운 board를 생성하는 방법이 시, 공간 복잡도 적으로 나은 선택이 됨.
    '''
    temp_board = [row[:] for row in board]  # 연구소 복사 (copy.deepcopy() 대신 빠른 복사)
    queue = deque(virus_positions)  # 초기 바이러스 위치 삽입

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and temp_board[nx][ny] == 0:  # 빈 칸에만 확산
                temp_board[nx][ny] = 2  # 바이러스 확산
                queue.append((nx, ny))

    # 안전 영역(0의 개수) 계산
    return sum(row.count(0) for row in temp_board)

def dfs(wall_count, index):
    global max_safe_area

    # 벽이 3개가 세워지면 BFS 실행
    if wall_count == 3:
        max_safe_area = max(max_safe_area, spread_virus())  # 안전 영역 갱신
        return

    # 빈 칸에서만 벽을 세움 (불필요한 중복 탐색 방지)
    for i in range(index, len(empty_spaces)):
        x, y = empty_spaces[i]
        board[x][y] = 1  # 벽 세우기
        dfs(wall_count + 1, i + 1)  # 다음 벽 세우기, 중복 탐색 방지
        board[x][y] = 0  # 백트래킹 (원상 복구)

T = int(input())
for tc in range(1, 1 + T):
    # 입력 받기
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 방향 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 빈 칸과 바이러스 위치 저장
    empty_spaces = []
    virus_positions = []

    '''
    1. 이 부분이 기존의 델타 탐색과 사용하는 visited와는 다름.
    2. 실제로 현재 경로를 따라 탐색할 필요 없기 때문에
        2-1. 0인 경우(빈 칸)만 벽을 세우는 경우의 수(부분 집합 dfs 구현)를 고려하면 되기에
        2-2. 0인 좌표만 따로 리스트(empty_spaces)로 받아 둠.
    3. 이후 0인 좌표에 대해서만 dfs를 적용하면 되기에 visited를 이용한 완탐보다 시간 복잡도와 공간 복잡도를 절약 가능.
    '''
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                empty_spaces.append((i, j)) # 이 부분
            elif board[i][j] == 2:
                virus_positions.append((i, j)) # 이 부분도 동일(?)

    # DFS로 벽 세우기 (최적화된 탐색)
    max_safe_area = 0

    # DFS 탐색 시작 (index 추가하여 중복 탐색 방지)
    dfs(0, 0)

    # 결과 출력
    print(max_safe_area)