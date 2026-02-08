import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==============================================================================
N = int(sys.stdin.readline())
mod = 1000000000
D = [0] * 1000001
D[1] = 0
D[2] = 1

# 완전 순열 점화식으로 풀이
for i in range(3, N + 1):
    D[i] = (i - 1) * (D[i - 1] + D[i - 2]) % mod

print(D[N])
#==============================================================================

e_t = time.time()
print("time: ", e_t - s_t)