import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

# DP
#==========================================================================
# 점화식
# D[i] = D[i - 2] + D[i - 1]
# 문자열로 풀면 문자열이 너무 길어짐. 쌍의 수를 리스트에 담아야 함.
# DP 리스트인 D는 K의 최댓값 길이의 리스트를 만든다.
cnt_A = [0] * 46
cnt_B = [0] * 46

# A를 위한 점화식
cnt_A[0] = 1
cnt_A[1] = 0
for i in range(2, 46):
    cnt_A[i] = cnt_A[i - 1] + cnt_A[i - 2]

# B를 위한 점화식
cnt_B[0] = 0
cnt_B[1] = 1
for i in range(2, 46):
    cnt_B[i] = cnt_B[i - 1] + cnt_B[i - 2]

# 입력값 받기
K = int(sys.stdin.readline())

# 정답 출력
print(cnt_A[K], cnt_B[K])
#==========================================================================

e_t = time.time()
print("time: ", e_t - s_t)