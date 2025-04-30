import heapq

# 힙에 탐색 시작지점을 추가.
queue = []
heapq.heappush(queue, (0, 1)) # cost, 출발 노드

ans = heapq.heappop(queue)
print(ans)
