import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#===================================================
nums = [i for i in range(21)]

for _ in range(10):
    start, end = map(int, sys.stdin.readline().split())

    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp

        start += 1
        end -= 1
    
print(*nums[1 : ])
#===================================================

e_t = time.time()
print("time: ", e_t - s_t)