import sys, time
sys.stdin = open("input.txt")
start = time.time()

#================================================
# 시간 복잡도: O(N^2)

from collections import defaultdict

# DFS
def DFS(node, nth, check):
    print(node, nth, check)
    if check == 1:
        return

    # nth가 4이면서 자식이 없다면 1 출력
    if nth == 4 and len(graph[node]) == 1:
        check = 1
        print(1)
        return True

    # mth가 5 이상인 경우는 필요없음.
    if nth >= 5:
        return

    # 방문했다면 생략
    if visited[node]:
        return
    # 아니라면 방문 체크
    visited[node] = True

    # 순회하면서 진행
    for child in graph[node]:
        DFS(child, nth + 1, check)

# 입력값을 받는다.
N, E = map(int, sys.stdin.readline().split())
edges = []
for _ in range(E):
    edges.append(list(map(int, sys.stdin.readline().split())))

# 양방향 그래프 구현
graph = defaultdict(list)
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

# DFS
visited = [False] * N
nth = 0
check = 0
for i in graph:
    DFS(i, nth, check)
#================================================

end = time.time()
print("time:", start - end)