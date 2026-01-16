import sys, time
sys.stdin = open("input.txt")
start = time.time()

# 시간 복잡도 완탐 가능.
# 모든 경로의 최단 시간이기에 heapq는 필요 없을듯?
#======================================================
from collections import defaultdict, deque
import heapq

# 입력 받기
N, E = map(int, sys.stdin.readline().split()) # 노드 수, 간선 수
K = int(sys.stdin.readline()) # 시작 노드
# 그래프 구현
graph = defaultdict(list)
for _ in range(E):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((cost, end))
# print(graph)

inf = 10**20
cost = [inf] * (N + 1)

# 탐색 로직
q = []
heapq.heappush(q, (0, K))
cost[K] = 0

while q:
    n_cost, now = heapq.heappop(q)
    for child in graph[now]:
        next_cost = min(cost[child[1]], n_cost + child[0])
        if next_cost == cost[child[1]]:
            continue
        cost[child[1]] = next_cost
        q.append((next_cost, child[1]))

for i in range(1, len(cost)):
    if cost[i] == inf:
        print("INF")
        continue
    print(cost[i])
#======================================================

end = time.time()
print("time: ", end - start)