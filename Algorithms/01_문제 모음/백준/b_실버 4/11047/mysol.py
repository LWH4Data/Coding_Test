import sys, time
sys.stdin = open("open.txt")
start = time.time()

#=====================================
# 입력값 받기
N, K = map(int, sys.stdin.readline().split())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))
cnt = 0
total = 0

# greedy로 풀이
for i in range(N-1, -1, -1):
    if K // numbers[i] >= 1:
        cnt += K // numbers[i]
        K = K % numbers[i]

    if K == 0:
        break

print(cnt)
#=====================================

end = time.time()
print("time: ", start - end)
