import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

# 점화식 구현하면 끝
#===========================================================
# 입력값 받기
T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    # DP 테이블 구현
    dp_table = [[0] * (n + 1) for _ in range(k + 1)]
    # 1호 채우기
    for i in range(k + 1):
        dp_table[i][1] = 1
    for i in range(1, n + 1):
        dp_table[0][i] = i
    
    # 점화식으로 남은 영역 채우기
    for i in range(1, k + 1):
        for j in range(2, n + 1):
            dp_table[i][j] = dp_table[i - 1][j] + dp_table[i][j - 1]
    
    print(dp_table[k][n])
#===========================================================

e_t = time.time()
print("time: ", e_t - s_t)