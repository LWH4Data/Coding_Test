import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=====================================================================
# 입력값 받기
M = int(sys.stdin.readline())
colors = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
N = sum(colors)

# 1개반 뽑는 경우 예외처리
flag = False
if K == 1:
    flag = True

# 색상이 1개인 경우 예외처리
if M == 1:
    flag = True

# 색상 리스트의 M개의 원소마다 K번의 확률을 계산하고 더한다.
# 연산 수행으로 답 구하기
result = 0
temp = 0
for m in range(M):
    result += temp
    temp = 1
    for k in range(K):
        temp *= (colors[m] - k) / (N - k)


print(result + temp)

# 점화식?
# print((5/18)*(4/17) + (6/18)*(5/17) + (7/18)*(6/17))
#=====================================================================

e_t =time.time()