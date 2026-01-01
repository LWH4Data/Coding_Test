import sys, time
sys.stdin = open("input.txt")
start = time.time()

#==================================================
import heapq

# 입력값 받기
N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
    heapq.heappush(numbers, int(sys.stdin.readline()))
ans = 0

# 알고리즘 수행
# numbers의 원소가 1이 아닐 때까지 반복
while len(numbers) != 1:
    # 가장 작은 두 수를 초기화한다.
    temp1 = heapq.heappop(numbers)
    temp2 = heapq.heappop(numbers)

    # 추출 한 두 수를 누적합 합한다.
    ans = ans + temp1 + temp2

    # 누적합을 다시 리스트에 넣고 반복한다.
    heapq.heappush(numbers, temp1 + temp2)

print(ans)
#==================================================

end = time.time()
print("time: ", end - start)