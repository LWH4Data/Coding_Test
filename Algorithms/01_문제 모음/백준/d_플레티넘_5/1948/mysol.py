import sys, time
sys.stdin = open("input.txt")
start = time.time()

#=====================================================
from collections import defaultdict
import heapq

# 입력값 받기
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = defaultdict(list)
cost = [0] * (n + 1)
# 그래프 구현
#   ● 튜플을 사용. (노드, 노드까지의 거리).
for _ in range(m):
    edge = list(map(int, sys.stdin.readline().split()))
    graph[edge[0]].append((edge[1], edge[2]))
# print(graph)

# 인디그리 구현
indegree = [0] * (n + 1)
for node in graph:
    for child in graph[node]:
        indegree[child[0]] += 1
# print(indegree)

# 끝 점과 시작점 받기
start, end = map(int, sys.stdin.readline().split())
# print(start, end)

# 다익스트라를 돌리되, 노드의 개수만 상태 저장.
q = []
for i in graph[1]:
    heapq.heappush(q, (i[0], -i[1]))
# print(q)

# 위상정렬을 하면서 
ans = []
visited = [0] * (n + 1)
while q:
    next, dist = q.pop()
    # print(next, dist)
    print(next, dist)
    if next == end:
        ans.append((next, dist))
    
    for child in graph[next]:
        temp = dist - cost[child[0]]
        if visited[child[0]] > temp:
            visited[child[0]] = temp
        else:
            continue
        
        indegree[child[0]] -= 1
        if indegree[child[0]] == 0:
            q.append((child, temp))

# print(ans)
# print(visited)
#=====================================================

end = time.time()
print("time: ", end - start)