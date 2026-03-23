import sys, time
start = time.time()
sys.stdin = open("input.txt")

#===========================================================
N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 누적합 grid 생성.
prefix = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] + grid[i - 1][j - 1] - prefix[i - 1][j - 1]

ans = 0
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans = prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
    print(ans)
#===========================================================

end = time.time()
print("time:", end-start)