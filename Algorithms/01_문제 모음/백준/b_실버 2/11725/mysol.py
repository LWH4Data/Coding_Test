import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

# 트리를 역으로(자 → 모) 구성하여 index로 저장하고, 마지막에 출력한다.
#===========================================================
from collections import defaultdict, deque

N = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(N-1):
    s, e = map(int, sys.stdin.readline().split())
    graph[e].append(s)
    graph[s].append(e)

# BFS를 돌리면서 부모 추가.
parents = [0] * (N + 1)
visited = [False] * (N + 1)

# BFS 준비
q = deque()
# 1이 루트 노드
q.append(1)
visited[1] = True

while q:
    now = q.popleft()
    
    for next in graph[now]:

        if visited[next]:
            continue
        visited[next] = True

        # 특정 노드를 탐색할 떄 양방향 그래프이기에 부모 노드가 next에 포함됨.
        # 따라서 이미 방문했다면 처리하지 않고 방문 안한 노드만 처리.
        parents[next] = now
        q.append(next)

for i in range(2, len(parents)):
    print(parents[i])
#===========================================================

e_t = time.time()
print("time: ", e_t - s_t)