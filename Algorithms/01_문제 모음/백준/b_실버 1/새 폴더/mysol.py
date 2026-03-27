import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==============================================
"""
누적합을 칸 수로 나누어 평균으로 구하기.
"""
R, C, Q = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 누적합 구현
prefix = [[0] * (C + 1) for _ in range(R + 1)]
for i in range(1, R + 1):
    for j in range(1, C + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] + grid[i - 1][j - 1] - prefix[i - 1][j - 1]

# Q 만큼 정답 계산.
total_sum = 0
total_cell = 0
ans = 0
for _ in range(Q):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    total_sum = prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
    
    # 총 칸의 수 계산
    total_cell = (x2 - x1 + 1) * (y2 - y1 + 1)
    ans = total_sum // total_cell
    print(ans)
#==============================================

e_t = time.time()
print("time: ", e_t - s_t)