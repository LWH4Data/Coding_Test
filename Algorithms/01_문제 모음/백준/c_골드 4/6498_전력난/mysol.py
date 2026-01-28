import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

# MST의 시간 복잡도 m log N 이내.
# 단순 MST 문제.
#==================================================================
from collections import defaultdict
import heapq

while True:
    # 입력값 받기
    N, E = map(int, sys.stdin.readline().split())
    if N == 0 and E == 0:
        break

    # 양방향 그래프 구현
    # 0번 노드부터 시작
    # 하면서 전체 합 계산
    total_sum = 0
    graph = defaultdict(list)
    for _ in range(E):
        s, e, w = map(int, sys.stdin.readline().split())
        total_sum += w
        graph[s].append((e, w))
        graph[e].append((s, w))

    # Prim 준비
    q = []
    heapq.heappush(q, (0, 1)) # weight, node
    result = 0
    visited = [False] * N

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

    print(total_sum - result)
#==================================================================

e_t = time.time()
print("time: ", e_t - s_t)