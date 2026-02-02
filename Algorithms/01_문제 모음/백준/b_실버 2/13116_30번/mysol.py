import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==========================================================================
from collections import defaultdict, deque

# << 함수 >> depth와 parent 찾는 BFS
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
        
            parent[next] = now
            depth[next] = depth[now] + 1
            q.append(next)

# << 함수 >> LCA 탐색 로직
def LCA(a, b):

    # b를 더 깊은 깊이로 설정
    if depth[a] > depth[b]:
        temp = a
        a = b
        b = temp

    # 깊이 맞추기
    while depth[a] != depth[b]:
        b = parent[b]

    # 같이 올리기
    while a != b:
        a = parent[a]
        b = parent[b]

    return a

T = int(sys.stdin.readline())

for tc in range(T):
    
    # 노드가 1이상 1023이하인 tree를 구현.
    tree = defaultdict(list)
    for i in range(1, 2**9):
        tree[i].append(2 * i)
        tree[i].append(2 * i + 1)

    # depth와 parent 찾기.
    depth = [0] * 1024
    parent = [0] * 1024
    visited = [False] * 1024

    # BFS로 탐색
    BFS(1)

    # LCA 탐색 로직
    a, b = map(int, sys.stdin.readline().split())
    print(LCA(a, b) * 10)
#==========================================================================

e_t = time.time()
print("time: ", e_t - s_t)