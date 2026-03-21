<<<<<<< HEAD
import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#======================================================================
N, M = map(int, sys.stdin.readline().split())
nums = [0] * (N + 1)

=======
import sys, time, copy
sys.stdin = open("input.txt")
s_t = time.time()

#===============================================================
N, M = map(int, sys.stdin.readline().split())

nums = [0] * (N + 1)
>>>>>>> eb1936d10f6dd120b848c12116584fcb3d20dccc
for i in range(N + 1):
    nums[i] = i

for _ in range(M):
<<<<<<< HEAD

    start, end, mid = map(int, sys.stdin.readline().split())

    temp = 
#======================================================================
=======
    start, end, mid = map(int, sys.stdin.readline().split())
    temp_start_mid = nums[start : mid].copy()
    temp_mid_end = nums[mid : end + 1].copy()
    print(temp_start_mid)
   
    for i in range(start, start + end + 1 - mid):
        nums[i] = temp_mid_end[i - 1]
    for i in range(start + end + 1 - mid, end + 1):
        print(i)
        nums[i] = temp_start_mid[i - 1]
    
    break
#===============================================================
>>>>>>> eb1936d10f6dd120b848c12116584fcb3d20dccc

e_t = time.time()
print("time: ", e_t - s_t)