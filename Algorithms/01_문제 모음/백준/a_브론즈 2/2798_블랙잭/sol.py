"""
3중 for loop을 순회할 때 i를 통해 전체 범위를 관리하여 중복을 방지한다.
→ 서로 다른 수를 고르는 조합이라 'N(N-1)(N-2) / 6'로 인해 
→ 시간 복잡도는 N^3으로 동일하나 6배 정도 차이가 난다.
"""

import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#===============================================================
"""
N의 크기로 보아 완전 탐색이 가능하다.
카드 3장을 고르는 문제이므로 순서가 아닌 조합으로 탐색한다.
"""

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

ans = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            temp = nums[i] + nums[j] + nums[k]

            if temp > M:
                continue

            ans = max(ans, temp)

print(ans)
#===============================================================

e_t = time.time()
print("time: ", e_t - s_t)