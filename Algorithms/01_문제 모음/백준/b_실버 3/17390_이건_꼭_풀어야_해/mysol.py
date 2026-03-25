import time, sys
sys.stdin = open("input.txt")
s_t = time.time()

#==============================================================
"""
일차원 리스트 누적합
"""

N, Q = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

# 누적합으로 구현
prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + A[i - 1]

# 누적합 리스트를 활용해 풀이.
ans = 0
for _ in range(Q):
    start, end = map(int, sys.stdin.readline().split())
    ans = prefix[end] - prefix[start - 1]
    print(ans)
#==============================================================

e_t = time.time()
print("time: ", e_t - s_t)