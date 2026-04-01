import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=====================================================================
"""
유클리드 호제법을 활용하여 해결한다.
"""

# 입력값 받기
A, B = map(int, sys.stdin.readline().split())

# 유클리드 호재법 사용
def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)

# 재귀아닌 while문 버전 
"""
def gcd(A, B):
    while B != 0:
        A, B = B, A % B
    return A
"""

# 대소 관계를 찾고 유클리드 호재법 적용
if A > B:
    ans = gcd(A, B)
else:
    ans = gcd(B, A)

# 결과 출력
print(ans)
# 최소공배수는 두 수를 곱하고 최대공약수로 나눔.
print(A * B // ans)
#=====================================================================

e_t = time.time()
print("time: ", e_t - s_t)