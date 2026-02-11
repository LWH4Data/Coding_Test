import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#===============================================================
# 1000000000 나누기 할 것.
# N에 따라 범위가 달라진다.
#   N은 100 이하 이기에 100개의 숫자까지 가능하다.

# mod 초기화
mod = 1000000000

# DP 테이블 초기화
D = [0] * 101

# DP 테이블 업데이트
D[1] = 9
for i in range(2, 101):
    D[i] = (D[i - 1] * 2 - i + 1) % mod

# 입력값 받기
N = int(sys.stdin.readline())
print(D[N])
#===============================================================

e_t = time.time()
print("time: ", e_t - s_t)