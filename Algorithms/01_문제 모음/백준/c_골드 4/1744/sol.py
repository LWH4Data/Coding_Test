import sys
sys.stdin = open("input.txt")
start = time.time()

#=============================================
import heapq

# 입력값 받기
N = int(sys.stdin.readline())
# 각 원소를 영역 별로 분할하여 저장한다.
num_pos = []
num_neg = []
one = 0
zero = 0

for i in range(N):
    data = int(sys.stdin.readline())

    # 1보다 큰 양수 원소인 경우
    #   - heapq는 오름차순 정렬이기에 -1을 곱해 가장 큰 양의 수가 첫 번째 원소가 되게 한다.
    if data > 1:
        heapq.heappush(num_pos, data * -1)

    # 1인 원소의 수를 저장한다.
    elif data == 1:
        one += 1
    
    # 0인 원소의 수를 저장한다.
    elif data == 0:
        zero += 1
    
    # 위의 경우가 아닌 경우는 음수이기에 음의 리스트에 입력한다.
    else:
        heapq.heappush(num_neg, data)

# 누적합 변수 초기화
sum = 0

# 양수 처리
while len(num_pos) > 1:
    first = heappop(num_pos) * -1
    second = heappop(num_pos) * -1
    sum += first * second

# 모두 처리하고 하나가 남은 경우 그대로 더해준다.
#   - 1 초과의 양수는 '음수, -1, 0, 1' 어떤 것과도 곱해질 수 없다.
if len(num_pos) > 0:
    sum += heapq.heappop(num_pos) * -1

# 음수 처리
while len(num_neg) > 1:
    first = heapq.heappop(num_neg)
    second = heapq.heappop(num_neg)
    sum += first * second

# 마찬가지로 음수가 남았다면 다음을 처리한다.
if len(num_neg) > 1:
    # 0이 없는 경우 음수가 상쇄되지 않기에 더한다.
    if zero == 0:
        sum += heapq.heappop(num_neg)

# 마지막으로 1의 개수를 더한다.
sum += one

print(sum)
#=============================================

end = time.time()
print("time: ", end - start)