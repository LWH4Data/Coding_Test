import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==============================================================
"""
- 3을 기준으로 완탐
"""
num = int(sys.stdin.readline())

check = 0
ans = 0

while 3 * check <= num:

    now_num = num - (3 * check)

    if now_num % 5 == 0:
        ans = check + now_num // 5
        break
    else:
        check += 1

if ans == 0:
    print(-1)
else:
    print(ans)
#==============================================================

e_t = time.time()
print("time: ", e_t - s_t)