import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#===========================================================
N, K = map(int, sys.stdin.readline().split())

# DP 테이블 생성
dp_table = [[0] * (N + 1) for _ in range(N + 1)]

# DP 테이플 초기값 채우기.
for i in range(N + 1):
    dp_table[i][1] = i
    dp_table[i][0] = 1
    dp_table[i][i] = 1

# DP 테이블 채우기
for i in range(2, N + 1):
    for j in range(1, i):
        dp_table[i][j] = dp_table[i-1][j-1] + dp_table[i-1][j]

print(dp_table[N][K] % 10007)
#===========================================================

e_t = time.time()
print("time: ", e_t - s_t)