import sys, time
sys.stdin = open("input.txt")
start = time.time()

#===============================================
import heapq

# 입력값 받기
N = int(sys.stdin.readline())
numbers = []
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    heapq.heappush(numbers, (e - s, s, e))

# end point를 기록할 변수
flag = 0
# 총 수를 기록할 변수
cnt = 0

while numbers:
    d, s, e = heapq.heappop(numbers)
    print(d, s, e)
    if flag <= s:
        cnt += 1
        flag = e
        print(flag)

print(cnt)

#===============================================

end = time.time()
print("time: ", end - start)