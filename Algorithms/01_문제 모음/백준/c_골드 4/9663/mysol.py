import sys, time
sys.stdin = open("input.txt")
start = time.time()

#==================================================
# 시간 복잡도: O(N^3), 전체 원소 * 전체 칸 * N 개의 깊이

# 방향 델타

# 십자 및 대각 위치 visited 구현.
def visit(x, y, N):
    i = 0
    while x - i >= 0:
        print(1)
        visited[x - i][y] = True
        i += 1

    i = 0
    while  x + i < N:
        visited[x + i][y] = True
        i += 1
    
    i = 0
    while y - i >= 0:
        print(1)
        visited[x][y - i] = True
        i += 1

    i = 0
    while y + i < N:
        visited[x][y + i] = True
        i += 1
    
    i = 0
    while x - i >= 0 and y - i >= 0:
        visited[x - i][y - i] = True
        i += 1
    
    i = 0
    while x - i >= 0 and y + i < N:
        visited[x - i][y + i] = True
        i += 1
    
    i = 0
    while x + i < N and y - i >= 0:
        visited[x + i][y - i] = True
        i += 1

    i = 0
    while x + i < N and y + i < N:
        visited[x + i][y + i] = True
        i += 1

# visited를 푸는 함수
def unvisit(x, y, N):
    i = 0
    while x - i >= 0:
        print(1)
        visited[x - i][y] = False
        i += 1

    i = 0
    while  x + i < N:
        visited[x + i][y] = False
        i += 1
    
    i = 0
    while y - i >= 0:
        print(1)
        visited[x][y - i] = False
        i += 1

    i = 0
    while y + i < N:
        visited[x][y + i] = False
        i += 1
    
    i = 0
    while x - i >= 0 and y - i >= 0:
        visited[x - i][y - i] = False
        i += 1
    
    i = 0
    while x - i >= 0 and y + i < N:
        visited[x - i][y + i] = False
        i += 1
    
    i = 0
    while x + i < N and y - i >= 0:
        visited[x + i][y - i] = False
        i += 1

    i = 0
    while x + i < N and y + i < N:
        visited[x + i][y + i] = False
        i += 1

# DFS
def DFS(N, depth):
    global ans

    if depth == N:
        ans += 1
        return

    # 전체 탐색
    for i in range(N):
        for j in range(N):
            # 방문했다면 반환
            if visited[i][j]:
                continue
            # 아니라면 방문 체크 후 DFS
            else:
                visit(i, j, N)
                DFS(N, depth + 1)
                # 끝났다면 다음을 위해 반환
                unvisit(i, j, N)

N = int(sys.stdin.readline())
depth = 0
ans = 0
visited = [[False] * N for _ in range(N)]

DFS(N, depth)

#==================================================

end = time.time()
print("time:", start - end)