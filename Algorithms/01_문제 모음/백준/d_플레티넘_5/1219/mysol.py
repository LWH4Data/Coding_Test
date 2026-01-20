import sys, time
sys.stdin = open("input.txt")
start_t = time.time()

#===========================================================
# ● 음수 사이클 외에 사이클을 찾아야할 거 같은데 구현을 못하겠음.

"""
< 변수 정리 >
- num_dosi: 도시의 수
- start_dosi: 시작 도시
- end_dosi: 끝 도시
- num_edge: 총 간선의 수
- cost: 누적 간선의 최단 거리
- profit: 특정 도시의 수익
"""
# 벨만-포드

# 입력값 받기
num_dosi, start_dosi, end_dosi, num_edge = map(int, sys.stdin.readline().split())
# 0번 도시부터 시작
cost = [sys.maxsize] * num_dosi
# edge 리스트 구현
edges = []
for _ in range(num_edge):
    edges.append(list(map(int, sys.stdin.readline().split())))
profit = list(map(int, sys.stdin.readline().split()))
money = 0

# 벨만-포드 알고리즘
cost[start_dosi] = 0
for _ in range(num_dosi - 1):
    for start, end, weight in edges:
        print(start, end, weight)
        if cost[start] != sys.maxsize and cost[end] > cost[start] + weight:
            cost[end] = cost[start] + weight
            # 누적 비용 계산
            money += profit[end]

# 음수 사이클 확인
mCycle = False

for start, end, weight in edges:
    if cost[start] != sys.maxsize and cost[end] > cost[start] + weight:
        mCycle = True
    
print(mCycle)

# 출력부 구현
if not mCycle:
    for i in cost:
        if i == sys.maxsize:
            print("gg")
            break
else:
    print(money - cost[end_dosi])

if mCycle:
    print("Gee")

print(cost)
print(money)
#===========================================================

end_t = time.time()
print("time: ", end_t - start_t)