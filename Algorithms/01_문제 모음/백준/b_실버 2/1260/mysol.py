import sys, time
sys.stdin = open("input.txt")
start = time.time()

#=============================================
from collections import defaultdict, deque

# DFS로 탐색 함수
def DFS(V):
    global ans_dfs

    # 방문 한 경우 넘기기
    if visited_dfs[V]:
        return

    # 현재 노드 출력
    ans_dfs.append(V)
    
    # 아닌 경우 방문 체크
    visited_dfs[V] = True
    for child in graph[V]:
        DFS(child)

    # 방문 노드 반환 X
    #   - 한 번의 탐색만 진행하도록 설계

def BFS():

    global ans_bfs

    # queue 세팅
    queue = deque()
    queue.append(V)
    ans_bfs.append(V)

    # 방문 체크
    visited_bfs[V] = True

    # BFS 탐색
    while queue:

        # 탐색 노드 받기
        node = queue.popleft()

        # 해당 노드의 자식 노드들 BFS 탐색
        for child in graph[node]:

            # 방문 했다면 skip
            if visited_bfs[child]:
                continue

            # 아니라면 정답에 추가
            ans_bfs.append(child)

            # 방문 체크
            visited_bfs[child] = True

            # 다음 탐색 후보로 추가.
            queue.append(child)

# 입력 받기
N, M, V = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
graph = defaultdict(list)
ans_dfs = []
ans_bfs = []
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

# graph의 value를 정렬 (순서 보장)
for i in graph:
    graph[i].sort()

# 방문 체크
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

# DFS 수행.
DFS(V)
print(*ans_dfs)
# BFS 수행.
BFS()
print(*ans_bfs)
#=============================================

end = time.time()
print("time:", start - end)