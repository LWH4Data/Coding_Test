import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==============================================================
from collections import defaultdict, deque

# find() 함수 생성.====================================
def find(a):
    # find를 하는 도중 del_node를 만난다면 del_node의 자식이므로
    # 제외.
    if parent[a] == del_node:
        return del_node

    # 노드 a가 부모가 없다면 조상을 찾은 것.
    if parent[a] == a:
        return a
    
    # 아니라면 조상까지 찾아서 올라감.
    else:
        parent[a] = find(parent[a])
        return parent[a]

# 풀이==========================================================
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
    
    if del_node == root:
        print(0)
        sys.exit()

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

        valid_child = 0
        
        # now에 자식이 있는 경우
        for next in graph[now]:

            # 자식 노드가 del_node인지 혹은 그 자손인지 확인한다.
            if next == del_node or find(next) == del_node:
                continue

            # 방문 여부를 체크한다.
            if visited[next]:
                continue
            visited[next] = True

            # next가 del_node도 아니고, 방문한 적이 없다면 탐색 가능한 자식이기에
            # q에 추가하고, 하단에서 leaf node로 추가되지 않도록 +1을 한다.
            valid_child += 1
            q.append(next)

        # now에 자식이 없는 경우는 leaf node이기에 +1을 하여 ans에 포함되지 않도록 한다.
        if valid_child == 0:
            ans += 1
        
    print(ans)
#==============================================================

e_t = time.time()
print("time: ", e_t - s_t)