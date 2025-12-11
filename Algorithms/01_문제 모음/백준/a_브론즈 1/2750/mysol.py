import sys, time
sys.stdin = open("input.txt")
start = time.time()

#===========================================
# 입력값 받기
N = int(sys.stdin.readline())
numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for i in range(len(numbers)):
    print(numbers[i])
#===========================================

end = time.time()
print("time:", start - end)