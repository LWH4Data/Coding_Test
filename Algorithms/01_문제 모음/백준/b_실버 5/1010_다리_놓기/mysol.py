import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

# 뽑아 두기만 하면 알아서 매핑되기에 조합만 구하면 된다.
#======================================================================
# 입력받기
T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    # M개중 N개이기에 M을 기준으로 DP 테이블을 생성한다.
    dp_table = [[0] * (M + 1) for _ in range(M + 1)]

    for i in range(M + 1):
        dp_table[i][i] = 1
        dp_table[i][1] = i
        dp_table[i][0] = 1
    
    # 점화식으로 DP 테이블 채우기.
    for i in range(2, M + 1):
        for j in range(1, i):
            dp_table[i][j] = dp_table[i - 1][j - 1] + dp_table[i - 1][j]

    print(dp_table[M][N])
#======================================================================

e_t = time.time()
print("time: ", e_t - s_t)