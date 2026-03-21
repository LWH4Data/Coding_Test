import sys, time, copy
sys.stdin = open("input.txt")
s_t = time.time()

#===============================================================
N, M = map(int, sys.stdin.readline().split())

nums = [i for i in range(N + 1)]

for _ in range(M):
    start, end, mid = map(int, sys.stdin.readline().split())
    nums[start : end + 1] = nums[mid : end + 1] + nums[start : mid]

print(*nums[1 : ])
#===============================================================

e_t = time.time()
print("time: ", e_t - s_t)