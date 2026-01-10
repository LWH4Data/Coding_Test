import sys, time
sys.stdin = open("input.txt")
start = time.time()

#=====================================================
# 최소공배수 함수
def sol(A, B):

    while B % A != 0:
        temp = A
        A = B % A
        B = temp

    return A

T = int(sys.stdin.readline())

for tc in range(1, T + 1):
    # print("test: ", tc)

    A, B = map(int, sys.stdin.readline().split())
    
    # 1이라면 답은 1이다.
    ans = sol(A, B)
    print(int(A * B / ans))
#=====================================================

end = time.time()
print("time: ", end - start)