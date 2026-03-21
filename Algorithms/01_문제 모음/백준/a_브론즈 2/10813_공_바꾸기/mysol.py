import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#====================================================
N, M = map(int, sys.stdin.readline().split())

nums = [i for i in range(N + 1)]

for _ in range(M):
    ball1, ball2 = map(int, sys.stdin.readline().split())
    temp = nums[ball1]
    nums[ball1] = nums[ball2]
    nums[ball2] = temp

print(*nums[1 : ])
#====================================================

e_t = time.time()
print("time: ", e_t - s_t)
