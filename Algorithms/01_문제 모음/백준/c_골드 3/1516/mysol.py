import sys, time
sys.stdin = open("input.txt")
start = time.time()

# N의 크기가 500 이하이기에 시간 복잡도는 문제가 되지 않음.
#==================================================================
from collections import defaultdict, deque

# 입력값 받기
N = int(sys.stdin.readline())
# index: 개별 노드, value: 해당 노드의 시간값
cost = [0] * (N + 1)
# 그래프의 구현
indegree = [0] * (N + 1)
graph = defaultdict(list)
for i in range(1, N + 1):
    temp = list(map(int, sys.stdin.readline().split()))
    # temp를 파싱하여 각 자료구조 구현
    for j in range(len(temp)):
        if temp[j] == -1:
            continue
        if j == 0:
            cost[i] = temp[j]
            continue
        graph[temp[j]].append(i)

# indegree 구현
for node in graph:
    for child in graph[node]:
        indegree[child] += 1

# 시작할 노드들을 취합.
search = []
for i in range(len(indegree)):
    if indegree[i] == 0:
        search.append(i)

del search[0]

# 탐색 시작
total_cost = [0]
q = deque()
for node in search:
    q.append((node, cost[node]))
    # 깊은 복사
    new_indegree = indegree.copy()

    while q:
        now, now_cost = q.popleft()
        total_cost.append(now_cost)

        for child in graph[now]:
            new_indegree[child] -= 1
            if new_indegree[child] == 0:
                q.append((child, now_cost + cost[child]))

del total_cost[0]

for ans in total_cost:
    print(ans)
#==================================================================

end = time.time()
print("time: ", end - start)