import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#========================================================================
# 해당 날을 선택했을 때와 하지 않았을 때를 나누어 DFS를 구현.

# DFS 함수 구현
# 해당 날짜와 가격을 통해 점화식을 구현한다.
def DFS(day, cost):
    global max_profit
    
    # 전체 날짜를 넘는 경우 skip
    if day > 7:
        return

    # 아닌 경우
    max_profit = max(max_profit, max_profit + cost)

    # 점화식
    for i in range(1, N):
        DFS(day + days[i] - 1, cost + costs[i] )

# 입력값 받기
N = int(sys.stdin.readline())
days = [0]
costs = [0]
dp_table = [0] * (N + 1)

# 각 정보 초기화.
for _ in range(N):
    day, cost = map(int, sys.stdin.readline().split())
    days.append(day)
    costs.append(cost)

# DFS를 통해 최대 수익 검수.
max_profit = 0
DFS(1, 10)
#========================================================================

e_t = time.time()
print("time: ", e_t - s_t)