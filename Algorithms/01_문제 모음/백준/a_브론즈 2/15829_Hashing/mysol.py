import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#===============================================================================
"""
주어진 수식 대로만 구현하면 된다.
"""
# 입력값 받기 및 초기 M 세팅
L = int(sys.stdin.readline())
words= str(sys.stdin.readline())
M = 1234567891

# 결과 변수 초기화
ans = 0

# i로 인덱스 관리하면서 연산 수행.
for i in range(L):
    ans += (ord(words[i]) - 96) * 31**i 
print(ans % M)
#===============================================================================

e_t = time.time()
print("time: ", e_t - s_t)