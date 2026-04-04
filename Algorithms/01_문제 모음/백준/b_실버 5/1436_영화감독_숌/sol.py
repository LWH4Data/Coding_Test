import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==================================================================================
N = int(sys.stdin.readline())

num = 666
nth = 0

while nth != N:
    
    if "666" in str(num):
        nth += 1
    num += 1

print(nth - 1)
#==================================================================================

e_t = time.time()
print("time: ", e_t - s_t)