import sys, time
sys.stdin = open("input.txt")
start = time.time()

#========================================================
from collections import defaultdict

# DFS 함수 구현 
#   - 시작 노드를 받아 전체 순환이 완료되면 +1
def DFS(node):
    # 방문 했다면 종료
    if check[node]:
        return
    
    # 방문한 노드가 아니라면 체크하고 DFS
    for child in graph[node]:
        # 방문 체크
        check[node] = True
        # DFS
        DFS(child)

    # 전체 순환 완료시 +1
    return 1

# 입력값 받기
N, E = map(int, sys.stdin.readline().split())
edges = []
for i in range(E):
    edges.append(list(map(int, sys.stdin.readline().split())))
ans = 0

# 양방향 그래프 구현
graph = defaultdict(list)
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

# 모든 정점에서 DFS
check = [False] * (N + 1)
for node in range(1, N + 1):
    # 방문 리스트 초기화
    if check[node]:
        continue
    ans += DFS(node)

print(ans)
#========================================================

end = time.time()
print("time:", start - end)