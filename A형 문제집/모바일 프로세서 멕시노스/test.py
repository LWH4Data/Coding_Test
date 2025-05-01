import sys
sys.stdin = open('sample_in.txt')
sys.setrecursionlimit(10**6)

# 방향: 상 하 좌 우
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def can_connect(v, h, dir):
    dy, dx = dirs[dir]
    y, x = v + dy, h + dx
    path = []

    while 0 <= y < N and 0 <= x < N:
        if graph[y][x] != 0:
            return []  # 전선이나 다른 코어에 막힘
        path.append((y, x))
        y += dy
        x += dx

    return path

def DFS(idx, connected, total_len):
    global max_connected, min_total_len

    if idx == len(core_list):
        if connected > max_connected:
            max_connected = connected
            min_total_len = total_len
        elif connected == max_connected:
            min_total_len = min(min_total_len, total_len)
        return

    v, h = core_list[idx]
    possible = False

    for dir in range(4):
        path = can_connect(v, h, dir)
        if not path:
            continue

        # 전선 설치
        for y, x in path:
            graph[y][x] = 2

        DFS(idx + 1, connected + 1, total_len + len(path))

        # 전선 제거 (백트래킹)
        for y, x in path:
            graph[y][x] = 0

        possible = True

    # 연결하지 않는 선택도 고려
    DFS(idx + 1, connected, total_len)

# 입력 처리
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 가장자리는 이미 연결된 상태로 간주 → 중앙에 있는 core만 대상으로
    core_list = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if graph[i][j] == 1:
                core_list.append((i, j))

    max_connected = 0
    min_total_len = float('inf')

    DFS(0, 0, 0)

    print(f"#{tc} 연결된 코어 수: {max_connected}, 전선 길이: {min_total_len}")
