import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

# 과거에는 BFS로 풀었는데 전체 노드 거리의 상태를 추적하기에 
# 플루이드-워셜이 더 쉽다 생각된다.
#===========================================================
N, E = map(int, sys.stdin.readline().split())
edges = []
for _ in range(E):
    edges.append(list(map(int, sys.stdin.readline().split())))

# 그래프 생성.
graph = [[sys.maxsize] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    graph[i][i] = 0

for s, e in edges:
    graph[s][e] = 1
    graph[e][s] = 1

# 업데이트
for k in range(N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(N + 1):
    for j in range(N + 1):
        if graph[i][j] == sys.maxsize:
            graph[i][j] = 0

ans = []
for i in range(1, N + 1):
    ans.append(sum(graph[i]))

print(ans.index(min(ans)) + 1)
#===========================================================

e_t = time.time()
print("time: ", e_t - s_t)