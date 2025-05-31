import sys, heapq
sys.stdin = open('input_11909.txt')

# 다익스트라 알고리즘
def dijkstra():
    dist[0][0] = 0
    heap = [(0, 0, 0)]  # (cost, v, h)
    
    while heap:
        cost, v, h = heapq.heappop(heap)

        if dist[v][h] < cost:
            continue

        for dv, dh in [(1, 0), (0, 1)]:
            nv, nh = v + dv, h + dh
            if 0 <= nv < N and 0 <= nh < N:
                # 비용 계산
                if graph[v][h] > graph[nv][nh]:
                    new_cost = cost
                else:
                    diff = graph[nv][nh] - graph[v][h] + 1
                    new_cost = cost + diff

                if dist[nv][nh] > new_cost:
                    dist[nv][nh] = new_cost
                    heapq.heappush(heap, (new_cost, nv, nh))

    return dist[N - 1][N - 1]

# 입력 처리
T = int(input())
for _ in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    dist = [[int(1e9)] * N for _ in range(N)]
    print(dijkstra())