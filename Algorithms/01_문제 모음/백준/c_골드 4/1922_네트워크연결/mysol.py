import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

# 단순 MST 구현 문제
#========================================================
from collections import defaultdict
import heapq

# 변수 선언
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

# Prim 준비
q = []
visited = [False] * (N + 1)

# 임의의 한 점 추가.
heapq.heappush(q, (0, 1))
result = 0

while q:
    now_weight, now_node = heapq.heappop(q)

    if visited[now_node]:
        continue
    visited[now_node] = True

    result += now_weight

    for next_node, next_weight in graph[now_node]:
        if visited[next_node]:
            continue
        heapq.heappush(q, (next_weight, next_node))

print(result)
#========================================================

e_t = time.time()
print("time: ", e_t - s_t)