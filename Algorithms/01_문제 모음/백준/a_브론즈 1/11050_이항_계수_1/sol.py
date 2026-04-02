import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#===========================================================
"""
DP를 통한 조합 풀이 정리.
"""
N, K = map(int, sys.stdin.readline().split())

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

for row in dp:
    print(row)

print(dp[N][K])
#===========================================================

e_t = time.time()
print("time: ", e_t - s_t)