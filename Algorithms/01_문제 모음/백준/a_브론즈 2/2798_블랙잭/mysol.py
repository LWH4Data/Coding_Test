import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#===============================================================
"""
N의 크기로 보아 완전 탐색이 가능하다.
DFS와 삼중 for loop을 사용하는 방법이 있다 생각되는데 for loop을 활용.
"""

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

# 3중 for loop
ans = 0
for i in range(N):
    for j in range(1, N):
        for k in range(2, N):

            # i, j, k 중 적어도 두 개가 같으면 skip
            if i == j or i == k or j == k:
                continue
            
            # M을 넘으면 skip
            temp = nums[i] + nums[j] + nums[k]
            if temp > M:
                continue

            # 아니라면 더 큰 값을 저장.
            ans = max(ans, temp)

print(ans)
#===============================================================

e_t = time.time()
print("time: ", e_t - s_t)