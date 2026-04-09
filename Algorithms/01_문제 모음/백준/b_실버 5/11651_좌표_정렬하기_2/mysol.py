import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=======================================================
N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    nums.append((a, b))

nums.sort(key=lambda x: (x[1], x[0]))
for i in range(N):
    print(*nums[i])
#=======================================================

e_t = time.time()
print("time: ", e_t - s_t)