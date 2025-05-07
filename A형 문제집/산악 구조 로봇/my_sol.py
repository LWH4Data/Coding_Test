import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#========================================================
import heapq 

# 델타 로직
dv = (-1, 1, 0, 0)
dh = (0, 0, -1, 1)

def dijkstra():
    
    # 초기값 초기화
    cost, v, h = 0, 0, 0
    dist[0][0] = graph[0][0]

    # 힙에 넣고 탐색 준비
    queue = []
    heapq.heappush(queue, ((cost, v, h)))

    # 탐색 시작
    while queue:
        cost, v, h = heapq.heappop(queue)

        # 만약 지금 탐색하는 비용이 이전까지의 비용보다 크다면 skip
        if dist[v][h] < cost:
            continue

        # 델타 구현
        for i in range(4):
            nv = v + dv[i]
            nh = h + dh[i]

            # 범위 넘어가면 skip
            if nv < 0 or nv >= N or nh < 0 or nh >= N:
                continue

            # 아니면 이동 시뮬 구현
            # 같은 경우
            temp = 0

            if graph[v][h] == graph[nv][nh]:
                temp += 1

            # 높은 경우
            elif graph[v][h] < graph[nv][nh]:
                temp = (graph[nv][nh] - graph[v][h]) * 2

            # 나머지
            else:
                temp = 0
            
            # 새로운 누적 비용이 현재 누적 비용보다 크다면 skip
            if dist[nv][nh] <= cost + temp:
                continue

            # 아니라면 업데이트 후 추가
            dist[nv][nh] = cost + temp
            heapq.heappush(queue, ((dist[nv][nh], nv, nh)))
    
    print(f"#{tc} {dist[N-1][N-1]}")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    dist = [[int(1e9)] * N for _ in range(N)]

    # 바로 다익스트라 함수 구현
    dijkstra()
#========================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
- 기본적인 다익스트라 + 시뮬

'''

'''
< 시간 복잡도 >
- 기본적인 다익스트라로 O(N^2logN^2)

'''

'''
< 문제 정의 >
1. Graph
    - 정사각형 지도(N). (4 <= N < 31)
        - 단, 1부터 N이기에 -> 0, N - 1로 정규화.
    - 각 셀에는 높이가 주어짐. (0 <= 높이 <= 9)

2. 이동 로직
    - 상, 하, 좌, 우

3. 비용
    - 높이가 같은 곳: -1
    - 낮은 곳: 0
    - 높은 곳: diff * 2

4. 최소 연료
    - dijkstra 사용.
'''