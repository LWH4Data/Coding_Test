import sys, time
sys.stdin = open("input.txt")
start = time.time()

#===============================================================
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().split())
# 앞에서부터 줄을 세운 결과이기에 순서대로 '부모 → 자식' 간의 관계가 된다.
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
indegree = [0] * (N + 1)
graph = defaultdict(list)
for edge in edges:
    graph[edge[0]].append(edge[1])

# 차수 구현
for node in graph:
    for child in graph[node]:
        indegree[child] += 1

# 탐색
q = deque()
ans = []

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
        ans.append(i)

while q:
    now = q.popleft()
    
    for child in graph[now]:
        indegree[child] -= 1

        if indegree[child] == 0:
            q.append(child)
            ans.append(child)

print(*ans)
#===============================================================

end = time.time()
print("time: ", end - start)