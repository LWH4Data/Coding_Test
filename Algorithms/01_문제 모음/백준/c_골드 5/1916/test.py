from collections import defaultdict
import heapq

queue = []

heapq.heappush(queue, ((0, 5)))
first, second = queue[0]
start, end = heapq.heappop(queue)

print(start, end)

print(first, second)