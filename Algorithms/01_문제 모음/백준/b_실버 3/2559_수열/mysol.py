"""
슬라이딩 윈도우 풀이
"""
import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=================================================================
N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

ans = -int(sys.maxsize)
sum_val = 0
for i in range(M):
    sum_val += nums[i]
ans = max(ans, sum_val)

for i in range(1, N - M + 1):
    sum_val = sum_val - nums[i - 1] + nums[i + M - 1]
    ans = max(ans, sum_val)

print(ans)
#=================================================================


e_t = time.time()

print("time: ", e_t - s_t)