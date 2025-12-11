import sys, time
sys.stdin = open("input.txt")
start = time.time()

# 절댓값 부분이 문제.

#===========================================
import heapq
# 입력 받기
N = int(sys.stdin.readline())
numbers = []
ans = []

# 입력 받는 만큼 반복
for i in range(N):

    # 분기에 따라 처리하기위해 일단 받은 값을 저장
    temp = int(sys.stdin.readline())

    # 0이 아닌 경우 일단 추가.
    if temp != 0:
        # heapq로 절댓값으로 우선 정렬하게 한 뒤, 부호를 기준으로 한 번 더 정렬.
        heapq.heappush(
            # 정렬 대상 리스트
            numbers, 
            # 튜플로 정렬 기준 우선순위를 전달. (절댓값, 실제값).
            (abs(temp), temp) 
            )
    
    # 0인 경우 pop하여 답 리스트에 추가.
    if temp == 0:
        # 빈 배열인 경우
        if not numbers:
            ans.append(0)
        # 아닌 경우
        else:
            ans.append(heapq.heappop(numbers)[1])

print(*ans)
#===========================================

end = time.time()
print("time:", start - end)