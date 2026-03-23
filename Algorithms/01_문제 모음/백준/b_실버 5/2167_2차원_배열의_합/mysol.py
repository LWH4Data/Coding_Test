import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==========================================================
N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 누적합 이차원 리스트
prefix = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + grid[i - 1][j - 1]

# K 번의 연산을 반복
K = int(sys.stdin.readline())
ans = 0
for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    ans = prefix[x][y] - prefix[i - 1][y] - prefix[x][j - 1] + prefix[i - 1][j - 1]
    print(ans)
#==========================================================

e_t = time.time()
print("time: ", e_t - s_t)