import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#======================================================================
N, M = map(int, sys.stdin.readline().split())
nums = [0] * (N + 1)

for i in range(N + 1):
    nums[i] = i

for _ in range(M):

    start, end, mid = map(int, sys.stdin.readline().split())

    temp = 
#======================================================================

e_t = time.time()
print("time: ", e_t - s_t)