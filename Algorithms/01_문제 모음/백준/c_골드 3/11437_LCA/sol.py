import sys, time
sys.stdin = open("input.txt")
s_t = time.time()


#=================================================================
from collections import defaultdict, deque

# << 함수 >>: BFS 탐색
def BFS(node):
    q = deque()
    q.append(node)
    visited[node] = True

    while q:
        now = q.popleft()

        for next in tree[now]:
            if visited[next]:
                continue
            visited[next] = True
            
            q.append(next)
            # index: 자식 노드, val: 부모 노드
            parent[next] = now
            # depth는 누적합을 통해 각 노드에 저장.
            depth[next] = depth[now] + 1

# << 함수 >>: LCA 수행 로직
def LCA(a, b):

    # 항상 b가 더 작은 depth를 갖는 노드가 되도록 설정.
    #   ● 즉, a가 더 낮은 곳에 위치
    if depth[a] < depth[b]:
        temp = a
        a = b
        b = temp
    
    while depth[a] != depth[b]:
        a = parent[a]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a

# 입력값 받기
N = int(sys.stdin.readline())

# 트리 구현
tree = defaultdict(list)
for _ in range(N - 1):
    s, e = map(int, sys.stdin.readline().split())
    tree[s].append(e)
    tree[e].append(s)

# 각 정보를 저장할 변수 초기화
depth = [0] * (N + 1)       # 깊이 정보
parent = [0] * (N + 1)      # 부모 노드의 정보
visited = [False] * (N + 1) # 방문 여부

# BFS를 하며 각 정보를 초기화
BFS(1)

# 알고리즘 수행 및 출력
M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(LCA(a, b))
#=================================================================

e_t = time.time()
print("time: ", e_t - s_t)