import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==================================================================
# 단순히 플루이드-워셜을 구현하고, 경로가 있는 노드는 1을, 없는 노드는 0을 출력한다.

# 입력값을 받는다.
N = int(sys.stdin.readline())
# 사이클을 판독해야 하기에 graph[i][i]를 0으로 초기화하지 않는다.
graph = [[sys.maxsize] * N for _ in range(N)]
temp = []
for _ in range(N):
    temp.append(list(map(int, sys.stdin.readline().split())))

edges = []
for i in range(N):
    for j in range(N):
        if temp[i][j] == 1:
            edges.append((i, j))

for i, j in edges:
    graph[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 사이클 판독이 필요.
for i in range(N):
    for j in range(N):
        if graph[i][j] == sys.maxsize:
            graph[i][j] = 0
        else:
            graph[i][j] = 1

for row in graph:
    print(*row)
#==================================================================

e_t = time.time()
print("time: ", e_t - s_t)