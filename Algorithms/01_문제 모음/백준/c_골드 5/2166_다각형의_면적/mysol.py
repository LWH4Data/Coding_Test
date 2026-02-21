import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=======================================================================
# CCW로 면접 구하는 문제
N = int(sys.stdin.readline())

# X와 Y의 리스트 생성.
X = []
Y = []
for _ in range(N):
    temp_X, temp_Y = map(int, sys.stdin.readline().split())
    X.append(temp_X)
    Y.append(temp_Y)

X.append(X[0])
Y.append(Y[0])

# CCW 연산
plus = 0
minus = 0
for i in range(0, N):
    plus += X[i] * Y[i + 1]
    minus += X[N - i] * Y[N - 1 - i]
print(round(abs(plus - minus) / 2, 1))
#=======================================================================

e_t = time.time()
print("time: ", s_t - e_t)