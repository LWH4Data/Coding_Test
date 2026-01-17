import sys, time
sys.stdin = open("input.txt")
start = time.time()

#==========================================================
"""
● Dijkstra는 queue에서 꺼낼 때, BFS는 queue에 넣을 때 visited 처리를 한다.
● BFS는 도착한 순간이 최단 거리인 반면, dijkstra는 최소 거리가 변경될 수 있기 때문이다.
"""

from collections import defaultdict
import heapq

# 입력값 및 자료구조 구현
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
visited = [False] * (N + 1)
cost = [sys.maxsize] * (N + 1)
graph = defaultdict(list)
for _ in range(M):
    start, end, c = map(int, sys.stdin.readline().split())
    # (자식 노드, 가중치)
    graph[start].append((end, c))
start, end = map(int, sys.stdin.readline().split())

# 탐색할 heapq 구현
q = []
heapq.heappush(q, (0, start))
cost[start] = 0

while q:
    dist, now = heapq.heappop(q)
    if visited[now]:
        continue
    visited[now] = True
    if now == end:
        print(dist)
        break

    # child[0]: 다음 노드
    # child[1]: 거리
    for child in graph[now]:
        temp = dist + child[1]

        if cost[child[0]] < temp:
            temp = cost[child[0]]
            # print(temp)
        else:
            cost[child[0]] = temp
        heapq.heappush(q, (temp, child[0]))
#==========================================================

end = time.time()
print("time: ", end - start)