import sys, time
sys.stdin = open("input.txt")
start = time.time()

#============================================================
# ● BFS와 union-find 모두 가능하지만, union-find가 경로 압축으로 더 빠르다.

# union-find 그래프 구현하고, 각 노드에서 find 함수를 했을 때 집합이 같은지.

# find 함수
def find(node):
    if parents[node] == node:
        return node
    else:
        parents[node] = find(parents[node])
        return parents[node]

# union 함수
def union(a, b):
    set_a = find(a)
    set_b = find(b)

    if set_a != set_b:
        parents[b] = set_a

# 입력값 받기.
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
# 이차원 리스트로 간선 정보 입력.
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# union-find를 위한 일차원 리스트
parents = [0] * (N + 1)

for i in range(1, N):
    for j in range(1, N):
        if graph[i]

#============================================================

end = time.time()
print("time: ", end - start)