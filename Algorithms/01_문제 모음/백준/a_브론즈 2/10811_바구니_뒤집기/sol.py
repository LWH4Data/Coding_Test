# 슬라이싱을 활용한 풀이

import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#===========================================================================
N, M = map(int, sys.stdin.readline().split())
nums = [0] * (N + 1)
for i in range(N + 1):
    nums[i] = i

for m in range(M):
    start, end = map(int, sys.stdin.readline().split())
    
    nums[start : end + 1] = nums[start : end + 1][ : : -1]
    
for i in range(1, len(nums)):
    print(nums[i], end=' ')
#===========================================================================

e_t = time.time()
print("time: ", e_t - s_t)