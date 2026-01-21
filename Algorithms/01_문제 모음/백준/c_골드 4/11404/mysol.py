import sys, time
sys.stdin = open("input.txt")
start_t = time.time()

#========================================================
# 모든 도시 쌍의 최단 거리 → 플로이드-워셜
num_dosi = int(sys.stdin.readline())
num_bus = int(sys.stdin.readline())
graph = [[sys.maxsize] * (num_dosi + 1) for _ in range(num_dosi + 1)]
for i in range(num_dosi + 1):
    for j in range(num_dosi + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(num_bus):
    start, end, weight = map(int, sys.stdin.readline().split())\
    # 중복 경로 중 더 작은 값을 받도록 설정.
    if graph[start][end] > weight:
        graph[start][end] = weight

for k in range(1, num_dosi + 1):
    for i in range(1, num_dosi + 1):
        for j in range(1, num_dosi + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, num_dosi + 1):
    for j in range(1, num_dosi + 1):
        if graph[i][j] == sys.maxsize:
            graph[i][j] = 0

del graph[0]

for row in graph:
    print(*row[1:])
#========================================================

end_t = time.time()
print("time: ",  end_t - start_t)