import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#================================================================================
# < 함수 >: 이동 연산을 전체 cell이 아니라 row와 column 단위로 처리하기 위한 함수.
def compress(line, n):

    # 1) 0이 아닌 숫자만 모아서 왼쪽으로 당긴 효과를 먼저 만든다.
    # 예: [2, 0, 2, 4] -> [2, 2, 4]
    nums = []
    # 행 혹은 열의 각 원소를 순회하며
    for x in line:
        # 0이 아닌 경우 nums에 추가.
        if x != 0:
            nums.append(x)

    # 최종 결과를 저장할 리스트
    result = []

    # nums를 앞에서부터 검사하기 위한 인덱스
    i = 0

    # nums를 순회하며 병합
    while i < len(nums):

        # 이동할 범위가 존재하고, 값도 같은 경우
        if i + 1 < len(nums) and nums[i] == nums[i + 1]:
            # 두 수를 합치고 result에 추가.
            # 예: [2, 2, 4] 에서 처음 2와 다음 2를 합쳐 4로 만든다.
            result.append(nums[i] * 2)
            # 두 개를 합쳤기에 i를 2칸 건너뛴다.
            i += 2

        # 다음 수와 현재 수가 다르다면 현재 수는 그대로 두고 result에 추가.
        else:
            result.append(nums[i])
            # 하나의 수만 이동하였기에 i를 한 칸 이동.
            i += 1
    
    # 2) result의 길이가 n이 될 때까지 뒤에 0을 붙인다. (빈 칸을 처리).
    # 예: [4, 4] -> [4, 4, 0, 0]
    while len(result) < n:
        result.append(0)
    
    return result

# < 함수 >: 이동 로직 (좌, 우, 상, 하) 구현==========================
def move(board: list, direction: int, n: int):
    """
    board를 direction 방향으로 한 번 이동시킨 새로운 보드를 반환

    direction:
    0 -> left
    1 -> right
    2 -> up
    3 -> down

    아이디어:
    - left는 각 행(row)을 그대로 compress
    - right는 각 행을 뒤집어서 compress 후 다시 뒤집기
    - up은 각 열(column)을 뽑아서 compress
    - down은 각 열을 뒤집어서 compress 후 다시 뒤집기
    """

    # 이동 후의 상태를 저장하기 위한 보드 생성.
    new_board = [[0] * n for _ in range(n)]

    # 0: left
    # 각 행을 그대로 왼쪽으로 압축한다.
    if direction == 0:
        for r in range(n):
            # board[r]는 r번째 행
            # 예: [2, 0, 2, 4] -> compress -> [4, 4, 0, 0]
            new_board[r] = compress(board[r], n)

    # 1: right
    # 오른쪽 이동은 입력 형식을 맞추어야 하기에 반전하여 수행.
    elif direction == 1:
        # 1) 행을 뒤집는다.
        for r in range(n):
            # 예: [2, 0, 2, 4]
            # 뒤집기 -> [4, 2, 0, 2]
            reversed_row = board[r][ : : -1]

            # 왼쪽 압축 수행
            # [4, 2, 0, 2] -> [4, 4, 0, 0]
            compressed = compress(reversed_row, n)
    
            # 다시 뒤집어서 원래 상태로 변환.
            # [4, 4, 0, 0] -> [0, 0, 4, 4]
            new_board[r] = compressed[ : : -1]
    
    # 2: up
    # 위쪽 이동은 열을 기준으로 왼쪽 압축과 같은 방식으로 처리한다.
    elif direction == 2:
        for c in range(n):
            # c번째 열을 위에서 아래 순서대로 뽑는다.
            # 예: [2, 0, 2, 4] 같은 열이 만들어질 수 있음
            col = []
            for r in range(n):
                col.append(board[r][c])

            # 위쪽으로의 이동은 그대로 compress 한다.
            compressed = compress(col, n)
            
            # 압축된 결과를 다시 new_board의 c 번째 열에 업데이트 한다.
            for r in range(n):
                new_board[r][c] = compressed[r]
    
    # 3: down
    # 아래쪽 이동은 오른쪽과 마찬가지로 열을 뒤집어 수행한다.
    elif direction == 3:
        # 열을 뒤집는다.
        for c in range(n):
            col = []
            for r in range(n):
                col.append(board[r][c])

            # 예: 아래 이동을 위해 열을 뒤집는다.
            # col[::-1] 한 뒤 compress 하고, 결과를 다시 뒤집는다.
            compressed = compress(col[ : : -1], n)[ : : -1]

            # 다시 c번째 열에 업데이트 한다.
            for r in range(n):
                new_board[r][c] = compressed[r]
    
    return new_board

# < 함수 >: 최댓값을 얻는 함수.
def get_max(board, n):
    """
    현재 board에서 가장 큰 블록 값 반환
    """
    max_val = 0
    for r in range(n):
        for c in range(n):
            if board[r][c] > max_val:
                max_val = board[r][c]
    return max_val

# < 함수 >: DFS 탐색 함수==========================================================
def dfs(depth: int, board: list, n: int): 

    # 최대 값을 관리하기 위한 전역변수 선언
    global ans

    # 현대 최댓값과 현재 주어진 board의 최댓값 중 더 큰 값으로 업데이트
    ans = max(ans, get_max(board, n))

    # 총 다섯 번의 이동을 다하면 백트래킹
    if depth == 5:
        return

    # 각 경우에 대해 탐색
    for d in range(4):
        next_board = move(board, d, n)
        dfs(depth + 1, next_board, n)

# 입력값 받기.
N = int(sys.stdin.readline())
graph = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dfs(0, graph, N)

print(ans)
#================================================================================

e_t = time.time()
print("time: ", e_t - s_t)