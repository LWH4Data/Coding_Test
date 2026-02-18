import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#====================================================================
# 입력값 받기 
# CCW를 위해 X와 Y의 자료 구조를 따로 만든다.
X = []
Y = []
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    X.append(x)
    Y.append(y)

# 첫 항을 한 번 더 추가.
X.append(X[0])
Y.append(Y[0])

# CCW 공식 적용
plus = 0
minus = 0
for i in range(3):
    plus += X[i] * Y[i + 1]
    minus += X[3 - i] * Y[3 - (i + 1)]

ans = plus - minus
if ans > 0:
    print(1)
elif ans == 0:
    print(0)
else:
    print(-1)
#====================================================================

e_t = time.time()
print("time: ", e_t - s_t)