import sys, time
sys.stdin = open('input_1584.txt')
start_time = time.time()

#================================================
import heapq 

# 델타 로직
dv = (-1, 1, 0, 0)
dh = (0, 0, -1, 1)

# dist에 넣을 최대 값 넣기
inf = int(1e9)

def dijkstra():
    
    # 최단 거리 배열 초기화
    dist = [[inf] * 501 for _ in range(501)]

    # 시작은 0임
    dist[0][0] = 0

    # 탐색 준비
    queue = []
    heapq.heappush(queue, (0, 0, 0)) # (비용, v, h)

    # dijkstra 탐색
    while queue:
        cost, v, h = heapq.heappop(queue)

        # 탐색 
        for d in range(4):
            nv = v + dv[d]
            nh = h + dh[d]

            # 범위 넘어가면 skip
            if nv < 0 or nv >= 501 or nh < 0 or nh >= 501:
                continue
            
            # 죽음 구역이면 못감.
            if graph[nv][nh] == 2:
                continue
            
            # 위험구역이면 비용 추가.
            if graph[nv][nh] == 1:
                temp = cost + 1
            else:
                temp = cost
            
            # 만약 이동할 좌표 dist[nv][nh]가 현재 누적 비용 temp 보다 작다면 skip
            if dist[nv][nh] <= temp:
                continue

            # 아니라면 dist[nv][nh] 업데이트하고 탐색 범위에 추가.
            dist[nv][nh] = temp

            # 추가
            heapq.heappush(queue, (dist[nv][nh], nv, nh))

    # dist[500][500]이 inf면 -1을 반환, 나머지는 그냥 반환
    if dist[500][500] == inf:
        print(-1)
    else:
        print(dist[500][500])

T = int(input())

for tc in range(1, T + 1):
    graph = [[0] * 501 for _ in range(501)]


    # 위험 구역
    N = int(input())
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        for v in range(min(x1, x2), max(x1, x2) + 1):
            for h in range(min(y1, y2), max(y1, y2) + 1):
                graph[v][h] = 1

    # 죽음의 구역
    M = int(input())
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        for v in range(min(x1, x2), max(x1, x2) + 1):
            for h in range(min(y1, y2), max(y1, y2) + 1):
                graph[v][h] = 2

    # dist 구현하고 dijkstra 순회하면서 최소 비용 반환
    dijkstra()
#==================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1
그래프 구현하고, 그냥 돌리면 될 듯.

'''

'''
< 시간 복잡도 >
1. 다익스트라 노드 갯 수의 log 값에 간선을 곱한다.
    -> O(E * log V)
    -> O(4 * log (501 * 501))
'''

'''
< 문제 정의 >
1. graph 특징
    - 죽음의 구역: 들어갈 수 없음.
    - 위험한 구역: 들어가서 한 번의 움직임 당 1의 생명력 감소.
    - 안전 구역: 생명 제한 없이 움직임. (위의 두 지역을 제외한 나머지)

2. (0, 0) 시작

3. (500, 500) 도착

4. 잃는 생명의 최솟값
    -> 최단 경로가 아닌 최소 비용.
    -> dijkstra
'''