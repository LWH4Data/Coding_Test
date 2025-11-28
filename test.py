# 1. 정점이 3개 있다고 가정(1~3번 사용)
#   ● graph[1], graph[2], graph[3] 각 정점의 인접 리스트 역할을 한다.
N = 3
graph = [[] for _ in range(N + 1)]

# 2. 정점 수와 간선 수 입력
N, E = map(int, input().split())

# 간선 정보를 입력받아 저장.
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

# 3. 그래프에서 데이터를 가져온다.
for nextNode, weight in graph[1]:
    print(f"next Node {nextNode}, weight = {weight}")