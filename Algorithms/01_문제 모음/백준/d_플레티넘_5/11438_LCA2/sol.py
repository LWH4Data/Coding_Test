import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

# 노드의 수(N)와 간선의 수(M)가 크기 때문에 빠른 LCA를 사용해야 한다.
#================================================================
from collections import defaultdict, deque

# << 함수 >> 트리 탐색을 위한 BFS
def BFS(node):
    q = deque()
    q.append(node)
    visited[node] = True
    level = 1     # 트리의 깊이
    now_size = 1  # 현재 깊이에서의 트리 크기
    count = 0     # 현재 깊이 트리크기 체크 변수

    while q:
        now = q.popleft()
        
        for next in tree[now]:
            if visited[next]:
                continue
            visited[next] = True
            q.append(next)

            parent[0][next] = now
            depth[next] = level
        
        count += 1

        # count한 수가 현재 깊이의 트리 크기와 같다면
        if count == now_size:
            # 다시 count = 0으로 초기화
            count = 0
            # 현재 깊이 트리의 크기도 앞으로 탐색할 수의 노드로 변경
            now_size = len(q)
            # 깊이도 한 층 더 깊어짐.
            level += 1

# << 함수 >> LCA 수행 함수.
def LCA(a, b):
    # b가 더 깊은 depth가 되도록 설정
    if depth[a] > depth[b]:
        temp = a
        a = b
        b = temp
    
    # 탐색하는 두 노드의 높이를 맞춘다.
    for k in range(kmax, -1, -1):
        # 2^k 만큼 위로 이동.
        if pow(2, k) <= depth[b] - depth[a]:
            # b의 부모의 깊이가 a보다 더 깊을 경우 (즉, b가 더 아래 존재)에만 올린다.
            if depth[a] <= depth[parent[k][b]]:
                b = parent[k][b]
    
    # a와 b가 같은 경우 최소 공통 조상이기에 출력.
    if a == b:
        return a
    
    # 아닌 경우 다시 탐색을 이어감.
    for k in range(kmax, -1, -1):
        # 같지 않은 공통 조상을 찾았다면 해당 위치로 이동.
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
    # 같지 않은 공통 조상의 하나 위의 조상이 공통 조상임.
    return parent[0][a]
        

# 입력값 받기
N = int(sys.stdin.readline())

# 트리 생성.
tree = defaultdict(list)
for _ in range(N- 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

# 필요한 변수 초기화
depth = [0] * (N + 1)
visited = [False] * (N + 1)
temp = 1
kmax = 0

# 높이 구하기
#   ● 2씩 곱하며 N 보다 커지기 직전까지 연산
while temp <= N:
    temp *= 2
    kmax += 1

# 부모 정보를 저장할 리스트 초기화.
#   ● 가로는 N + 1 노드의 수만큼,
#   ● 세로는 kmax + 1 깊이의 수만큼.
parent = [[0] * (N + 1) for _ in range(kmax + 1)]

# BFS를 통해 트리를 탐색하며 정보 업데이트
BFS(1)

# 점화식을 통해 부모 정보 리스트 업데이트
for k in range(1, kmax + 1):
    for n in range(1, N + 1):
        parent[k][n] = parent[k - 1][parent[k - 1][n]]

# 알고리즘 시작.
M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(str(LCA(a, b)))
#================================================================

e_t = time.time()
print("time: ", e_t - s_t)