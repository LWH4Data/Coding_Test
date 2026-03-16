import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#================================================
N, M = map(int, sys.stdin.readline().split())

nums = [0 for _ in range(N + 1)]

for _ in range(M):
    start, end, delta = map(int, sys.stdin.readline().split())
    
    for i in range(start, end + 1):
        nums[i] = delta

print(*nums[1 : ])
#================================================

e_t = time.time()
print("time: ", e_t - s_t)