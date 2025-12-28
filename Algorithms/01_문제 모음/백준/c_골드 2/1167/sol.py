import sys, time
sys.stdin = open("input.txt")
start = time.time()

#=================================================
# < 풀이 >
# 임의의 노드에서 BFS를 통해 가장 먼 노드를 찾는다. (끝점 찾기).
# → 찾은 끝점에서 다시 BFS를 돌려 가장 먼 노드를 찾는다. (가장 긴 지름 찾기).
# → 해당 거리를 출력한다.
from collections import defaultdict, deque

# 입력값 받기
N = int(sys.stdin.readline().strip())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 양방향 그래프 초기화
graph = defaultdict(list)
for edge in edges:
    for i in range(1, len(edge), 2):
        if edge[i] == -1:
            break
        else:
            graph[edge[0]].append((edge[i], edge[i + 1]))
            graph[edge[i]].append((edge[0], edge[i + 1]))

# 거리를 담을 리스트 초기화
dist = [0] * (N + 1)
# 방문 리스트 초기화
visited = [False] * (N + 1)

# BFS 구현
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] =  True

    # 탐색 시작
    while queue:
        
        now = queue.popleft()
        
        # 자식 노드들을 순회하면서 확인
        for child in graph[now]:
            # append 하기 전에 방문체크.
            if visited[child[0]]:
                continue
            visited[child[0]] = True
            queue.append(child[0])
            # append 되었다면 현재 노드 거리는
            # → 이전 노드의 거리(dist[now]) + 현재 노드의 거리(child[1])
            dist[child[0]] = dist[now] + child[1]

# 임의의 노드에서 BFS 1회
BFS(1)
# 답을 찾기위한 변수 Max 초기화
Max = 1

# BFS 1회 후 가장 먼 노드를 찾아 Max에 초기화
for i in range(2, N + 1):
    if dist[Max] < dist[i]:
        Max = i

# 새로운 BFS를 위한 변수 초기화
dist = [0] * (N + 1)
visited = [False] * (N + 1)
# 1회 BFS에서 찾은 최대 노드로 한 번 더 BFS
BFS(Max)

# 정렬 후 가장 마지막 노드의 값을 출력하면 가장 큰 거리(지름)을 알 수 있다.
dist.sort()
print(dist[N])
#=================================================

end = time.time()
print("time:", start - end)