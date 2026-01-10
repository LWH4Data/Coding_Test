import sys, time
sys.stdin = open("input.txt")
start = time.time()

#=================================================
from collections import defaultdict, deque

# 탐색 BFS
def BFS(X, k = 0):
    q = deque()
    q.append((X, k))
    visited[X] = True

    while q:
        now, new_k = q.popleft()
        # 찾는 거리인 경우에만 정답 리스트에 저장.
        if new_k == K:
            ans.append(now)

        for child in graph[now]:
            if visited[child]:
                continue
            visited[child] = True
            q.append((child, new_k + 1))

# 입력값 받기
N, M, K, X = map(int, sys.stdin.readline().split())
# 간선 정보 받기
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
visited = [0] * (N + 1)
ans = list()

# 방향 그래프 구현
graph = defaultdict(list)
for edge in edges:
    graph[edge[0]].append(edge[1])

# 탐색을 하면서 각 노드와 거리를 확인.
BFS(X, k=0)

# 출력 전 오름차순 정렬
ans.sort()

# BFS의 결과를 기반으로 출력 
# 해당하는 노드가 없는경우 -1을 출력
if not ans:
    print(-1)
# 노드가 있다면 다음 노드가 없는 걸 확인하고 출력.
else:
    for i in ans:
        print(i)
#=================================================

end = time.time()
print("time: ", start - end)