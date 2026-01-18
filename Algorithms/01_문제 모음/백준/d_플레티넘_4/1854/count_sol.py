import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

count = [0] * (n + 1)
ans = [-1] * (n + 1)

pq = [(0, 1)]  # (경로비용, 노드)

while pq:
    cost, u = heapq.heappop(pq)
    count[u] += 1

    if count[u] == k:
        ans[u] = cost
    if count[u] > k:
        continue  # k번 넘게 나온 노드는 더 확장 X

    for v, w in graph[u]:
        heapq.heappush(pq, (cost + w, v))

for i in range(1, n + 1):
    print(ans[i])
