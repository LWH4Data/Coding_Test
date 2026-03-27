import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#===============================================================
N = int(sys.stdin.readline())

count = 1
range_end = 1

while N > range_end:
    range_end += 6 * count
    count += 1

print(count)
#===============================================================

e_t = time.time()
print("time: ", e_t - s_t)