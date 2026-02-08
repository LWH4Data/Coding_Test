import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#========================================================================
N = int(sys.stdin.readline())
cnt = 0

while N != 1:

    if N % 3 == 0:
        N //= 3
        cnt += 1
    
    if N % 2 == 0:
        N //= 2
        cnt += 1
    
    else:
        N -= 1
        cnt += 1

print(cnt)
#========================================================================

e_t = time.time()
print("time: ", e_t - s_t)