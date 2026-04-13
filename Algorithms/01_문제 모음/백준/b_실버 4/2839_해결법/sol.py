"""
- 최솟값을 찾기 때문에 5를 기준으로 하는 풀이가 더 적합함.
"""

import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==============================================================
num = int(sys.stdin.readline())

check = num // 5
ans = -1

while check >= 0:

    now_num = num - (5 * check)

    if now_num % 3 == 0:
        ans = check + now_num // 3
        break
    else:
        check -= 1

print(ans)
#==============================================================

e_t = time.time()
print("time: ", e_t - s_t)