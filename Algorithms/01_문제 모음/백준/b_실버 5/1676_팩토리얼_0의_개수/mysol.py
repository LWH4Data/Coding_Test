import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==============================================================
"""
계산은 O(1)이기에 연산하고 0개수 세기.
"""
N = int(sys.stdin.readline())
num = 1
for i in range(1, N + 1):
    num *= i

num = str(num)

ans = 0
for i in range(len(num) - 1, -1, -1):
    if num[i] == '0':
        ans += 1
    else:
        break

print(ans)
#==============================================================

e_t = time.time()
print("time: ", e_t - s_t)