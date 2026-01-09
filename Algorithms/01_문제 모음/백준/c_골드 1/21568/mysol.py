import sys, time
sys.stdin = open("input.txt")
start = time.time()

#================================================
# gcd 함수 구현.
def gcd(A, B):
    while B % A != 0:
        print(1)
        temp = A
        X.append(B // A)
        A = B % A
        Y.append(A)
        B = temp
    
    return A

# 해를 찾는 함수.
def sol(X, Y):
    for i in range(len(X)):
        temp_y = y
        y = x - y * X[i]
        x = temp_y

# 입력값 받기
A, B, C = map(int, sys.stdin.readline().split())
if A > B:
    temp_s = B
    B = A
    A = temp_s
X = []
Y = []

if B % A == 0:
    x = 1
    y = 0
else:
    gcd(A, B)


# 
if X:
    sol(x, y)

#-----------------------------------------------
# 배수 K를 찾아 현재 C에 맞는 nx와 ny를 구하는 영역
nx = 0
ny = 0
i = 1
while A*nx + B*ny != C:
    nx = x * i
    ny = y * i
    i += 1
    
print(nx, ny)

# gcd를 통해 몫과 나머지의 정보를 저장해 둔다.

# 저장한 정보를 역으로 계산하며 최종 X와 Y를 찾는다.
#================================================

end = time.time()
print("time: ", end - start)