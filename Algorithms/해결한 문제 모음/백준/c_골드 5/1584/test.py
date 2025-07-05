import heapq

queue = []
heapq.heappush(queue, (0, 0, 0)) # (비용, v, h)
heapq.heappush(queue, (1, 0, 0)) # (비용, v, h)

print(queue)