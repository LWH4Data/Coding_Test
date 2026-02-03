import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==============================================================
from collections import defaultdict
import heapq

# 압력값 받기
N, M, T = map(int, sys.stdin.readline().split())

# 양방향 그래프 생성.
graph = defaultdict(list)

for _ in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

# 탐색 시작.
q = []
heapq.heappush(q, (0, 1))
visited = [False] * (N + 1)
result = 0
cnt = 0

while q:
    now_weight, now_node = heapq.heappop(q)


    if visited[now_node]:
        continue
    visited[now_node] = True

    result += now_weight

    for next_node, next_weight in graph[now_node]:
        heapq.heappush(q, (next_weight + T, next_node))

print(result)
#==============================================================

e_t = time.time()
print("time: ", e_t - s_t)