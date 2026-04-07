import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#===============================================================
N = int(sys.stdin.readline())

nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
nums.sort()

for i in range(N):
    print(nums[i])
#===============================================================

e_t = time.time()
print("time: ", e_t - s_t)