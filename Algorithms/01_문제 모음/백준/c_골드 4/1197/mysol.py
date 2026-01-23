import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==================================================================
# MST를 프림으로 구현한다.
#   ● 크루스컬로 구현하면 Python에서는 recursion 문제가 발생할 수 있다.
#   ● 다익스트라는 특정 노드에서 다른 노드까지의 최단 경로(누적합)을 탐색하기에
#     프림처럼 pop 시점에 visited를 확인하지 않는다.
#   ● 프림은 단일 간선 정보를 활용하기에 중복 노드가 나온다면 이미 해당 노드의
#     최단 경로를 확인하였기에 visited를 체크한다.
from collections import defaultdict
import heapq

N, E = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((w, e))
    graph[e].append((w, s))
visited = [False] * (N + 1)

q = []
heapq.heappush(q, (0, 1))

# MST의 전체 비용
result = 0
# MST에 포함된 노드 수
cnt = 0

# 전체를 탐색
while q:
    nw, nn = heapq.heappop(q)

    # 방문한 노드라면 skip
    #   ● 이미 해당 노드의 최소 간선을 방문했기에 확인하지 않는다.
    if visited[nn]:
        continue
    visited[nn] = True

    # 방문하지 않았다면 최소 가중치 누적합
    result += nw

    # 다음 노드를 순회하면서 업데이트
    for cw, cn in graph[nn]:
        if visited[cn]:
            continue
        heapq.heappush(q, (cw, cn))
    
print(result)
#==================================================================

e_t = time.time()
print("time: ", e_t - s_t)