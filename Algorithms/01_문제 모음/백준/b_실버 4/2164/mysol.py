import sys, time
from collections import deque
sys.stdin = open("input.txt")
start = time.time()

#====================================
# 입력값 받기
N = int(sys.stdin.readline())
numbers = deque()

# deque로 자료 구조 구현
for  i in range(1, N + 1):
    numbers.append(i)

# numbers에 숫가자 하나 남울 때까지 반복
while len(numbers) != 1:

    # 수 제거 로직
    numbers.popleft()
    # 수가 하나 남는담녀 종료
    if len(numbers) == 1:
        break

    # 상단 수 하단으로 추가 로직
    numbers.append(numbers.popleft())

# 정답 출력
print(*numbers)
#====================================

end = time.time()
print("time:", start - end)