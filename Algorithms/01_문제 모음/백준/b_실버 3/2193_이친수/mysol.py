import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

# DP
# ● 왜인지 모르겠는데 D[i] = D[i - 2] + D[i - 1]이 된다.
#====================================================================
# 점화식 리스트 초기화.
D = [0] * 91

# 점화식 리스트 채우기
D[1] = 1
D[2] = 1
for i in range(3, 91):
    D[i] = D[i - 2] + D[i - 1]

# 입력값 받기
N = int(sys.stdin.readline())

# 정답 출력
print(D[N])
#====================================================================

e_t = time.time()
print("time: ", e_t - s_t)