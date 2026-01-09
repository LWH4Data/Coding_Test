import sys, time
sys.stdin = open("input.txt")
start = time.time()

# 노드의 수가 간선의 수보다 많고, 비순환 그래프이기에 시간복잡도는 노드 기준 브루트포스O(N^2)?

#=========================================================
from collections import defaultdict, deque

# BFS 탐색 함수
def BFS(start):
    
    visited = [False] * (N + 1)

    q = deque()
    q.append(start)
    visited[start] = True

    cnt = 0

    while q:
        now = q.popleft()
        
        for child in graph[now]:
            if visited[child]:
                continue
            visited[child] = True
            cnt += 1
            q.append(child)

    return cnt 

# 입력값 받기
N, E = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
# 방향 그래프 구현
#   - 부모 노드가 두 번째 원소에 옴을 주의
graph = defaultdict(list)
for edge in edges:
    graph[edge[1]].append(edge[0])

# 각 노드에서 BFS 진행
numbers = [0]
# BFS 함수에서 나온 총 방문 노드의 수를 저장.
for i in range(1, N + 1):
    numbers.append(BFS(i))

# 최대값을 받고 방문 노드 수를 순회하면서 index 기준 출력.
max_val = max(numbers)
for i in range(1, N + 1):
    if numbers[i] == max_val:
        print(i, end = ' ')
#=========================================================

end = time.time()
print("time: ", end - start)