import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#======================================================
N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 누적합 이차원 리스트 초기화
prefix = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] + grid[i - 1][j - 1] - prefix[i - 1][j - 1]

# 누적합 연산.
K = int(sys.stdin.readline())
ans = 0
for _ in range(K):
    # 1-index
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans = prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
    print(ans)
#======================================================

e_t = time.time()
print("time: ", e_t - s_t)