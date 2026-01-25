import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

# 최소 신장 트리를 구현하고

# 마지막에 가장 큰 가중치를 뺀다(두 마을을 분기).
#================================================================================
from collections import defaultdict
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))
    graph[e].append((s, w))
visited = [False] * (N + 1)

# 탐색 시작점
q = []
heapq.heappush(q, (0, 1))
result = 0
now_max = 0

while q:
    
    now_weight, now_node = heapq.heappop(q)
    
    if visited[now_node]:
        continue
    visited[now_node] = True

    result += now_weight
    now_max = max(now_max, now_weight)

    for next_node, next_weight in graph[now_node]:

        if visited[next_node]:
            continue
        heapq.heappush(q, (next_weight, next_node))

print(result - now_max)
#================================================================================

e_t = time.time()
print("time: ", e_t - s_t)