import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==============================================================
from collections import defaultdict, deque

# find() 함수 생성.
def find(a):
    if parent[a] == 2:
        return 2

    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


# 입력값 받기.
N = int(sys.stdin.readline())
if N == 1:
    print(0)
else:
    parents_list = list(map(int, sys.stdin.readline().split()))
    # 트리를 구현
    graph = defaultdict(list)
    for i in range(len(parents_list)):
        if parents_list[i] == -1:
            root = i
        else:
            graph[parents_list[i]].append(i)

    # 삭제될 노드와 그 자식들을 find() 함수로 삭제
    del_node = int(sys.stdin.readline())
    
    # 부모 노드를 관리할 parent 리스트 구현. (0부터 시작).
    parent = [0] * N
    for i in range(N):
        parent[i] = i
    for i in range(N):
        for child in graph[i]:
            parent[child] = i

    # BFS 돌리면서 정답 체크
    q = deque()
    q.append(root)
    ans = 0
    visited = [False] * N
    visited[root] = True

    while q:
        now = q.popleft()

        for next in graph[now]:
            if next == del_node and len(graph[next]) == 1:
                ans += 1

            if next == del_node or find(next) == del_node:
                continue
            
            if visited[next]:
                continue
            visited[next] = True
            
            if not graph[next]:
                ans += 1
            
            
            q.append(next)
    print(ans)
    # find를 통해 지워야 하는 노드의 모든 자식들을 업데이트 한다.

    # root부터 BFS를 돌린다.
        
        # parents가 지우는 노드인 경우에는 탐색을 하지 않는다.

        # 탐색을 하지 않는 노드이거나 자식이 없는 노드인 경우를 카운트한다. 
#==============================================================

e_t = time.time()
print("time: ", e_t - s_t)