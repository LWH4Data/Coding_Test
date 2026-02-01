import sys, time
sys.stdin = open("input.txt")
s_t = time.time()


#=================================================================
from collections import defaultdict, deque

#=================================================================
def LCA(a, b):
    flag = True

    while lca_list[a][1] != lca_list[b][1]:
        if lca_list[a][1] > lca_list[b][1]:
            a = lca_list[a][0]
            if a == b:
                print(a)
                flag = False
    
        else:
            b = lca_list[b][0]
            if a == b:
                print(a)
                flag = False
    
    while lca_list[a][0] != lca_list[b][0]:
        a = lca_list[a][0]
        b = lca_list[b][0]
    
    if flag:
        print(lca_list[a][0])


# 입력값 받기
N = int(sys.stdin.readline())

# BFS를 위한 트리 만들기
tree = defaultdict(list)
for i in range(N - 1):
    parent, child = map(int, sys.stdin.readline().split())
    tree[parent].append(child)
    tree[child].append(parent)

lca_list = [0] * (N + 1)
q = deque()
q.append(1) # node, depth
visited = [False] * (N + 1)
visited[1] = True
test = defaultdict(list)

while q:
    now = q.popleft()
    
    for next in tree[now]:

        if visited[next]:
            continue
        visited[next] = True

        test[now].append(next)
        q.append(next)

lca_list = [0] * (N + 1)
lca_list[1] = (1, 0)  # 루트 노드 초기화
q = deque()
q.append((1, 0)) # node, depth
visited = [False] * (N + 1)
visited[1] = True

while q:
    now, depth = q.popleft()
    
    for next in test[now]:

        if visited[next]:
            continue
        visited[next] = True

        lca_list[next] = (now, depth + 1)
        q.append((next, depth + 1))

M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    LCA(a, b)
#=================================================================

e_t = time.time()
print("time: ", e_t - s_t)