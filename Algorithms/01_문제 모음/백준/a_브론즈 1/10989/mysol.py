import sys, time
sys.stdin = open("input.txt")
start = time.time()

#=======================================================
# 입력값 받기
N = int(sys.stdin.readline())

#=======================================================

end = time.time()
print("time:", start - end)