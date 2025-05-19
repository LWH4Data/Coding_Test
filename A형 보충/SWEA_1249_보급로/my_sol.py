import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#================================================
import heapq

# 델타 
dv = (-1, 1, 0, 0)
dh = (0, 0, -1, 1)

def dijkstra():
    
    # 시작 비용은 0
    dist[0][0] = graph[0][0]

    # 탐색 queue 생성
    queue = []
    # 시작 좌표(0, 0)와 cost(0)을 입력
    # (cost, v, h)
    heapq.heappush(queue, ((graph[0][0], 0, 0)))

    # 탐색 시작
    while queue:
        cost, v, h = heapq.heappop(queue)

        # cost가 더 작은 경우만 탐색
        if dist[v][h] < cost:
            continue

        # 델타 탐색
        for i in range(4):
            temp = 0
            nv = v + dv[i]
            nh = h + dh[i]

            # 범위 초과시에 skip
            if nv < 0 or nv >= N or nh < 0 or nh >= N:
                continue

            # 비용이 넘는 경우 탐색 skip
            temp = cost + graph[nv][nh]
            if dist[nv][nh] <= temp:
                continue

            # 아니면 탐색 추가.
            dist[nv][nh] = temp
            heapq.heappush(queue, ((temp, nv, nh)))

    print(f'#{tc} {dist[N-1][N-1]}')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().strip())) for _ in range(N)]
    dist = [[int(1e9)] * N for _ in range(N)]

    # 다익스트라 구현
    dijkstra()
#================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >

'''

'''
< 시간 복잡도 >
- O(N^2logN^2)

'''

'''
< 문제 정의 >
1. 도로 복구 - 깊이에 비례하여 복구 시간 증가 - 복구 시간이 가장 짧은 경로의 복구 시간
    - 값 1마다 복구 시간도 1

2. 단순 다익
'''