import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#============================================================
# DP
#   ● DP 테이블의 idx: n, val: 총 갯수
#   ● 노가다로 구하면 D[i] = D[i - 2] + D[i - 1]

# DP 테이블 초기화.
D = [0] * 1001

# DP 테이블 업데이트
D[1] = 1
D[2] = 2
for i in range(3, 1001):
    D[i] = (D[i - 2] + D[i - 1]) % 10007

# 입력값 받기
N = int(sys.stdin.readline())

# 정답 출력
print(D[N])
#============================================================

e_t = time.time()
print("time: ", e_t - s_t)