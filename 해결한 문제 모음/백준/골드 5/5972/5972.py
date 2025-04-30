import sys, time 
sys.stdin = open('input_5972.txt')
start_time = time.time()

#====================================================
from collections import defaultdict
import heapq

def dijkstra():

    # 일단 출발 지점의 비용은 0임
    dist[1] = 0
    temp = 0

    # 힙에 탐색 시작지점을 추가.
    queue = []
    heapq.heappush(queue, (0, 1)) # cost, 출발 노드

    # dijkstra 시작
    while queue:
        cost, cur = heapq.heappop(queue)

        # 이전 비용보다 크면 일단 탐색 자체를 안함
        if dist[cur] < cost:
            continue

        # 탐색
        for neighbor, cost in graph[cur]:
            
            # 현재까지의 비용이 이전 이용보다 크면 skip
            temp = dist[cur] + cost
            if dist[neighbor] <= temp:
                continue
            
            # 아니면 업데이트 후 추가
            dist[neighbor] = temp
            heapq.heappush(queue, (temp, neighbor))

N, M = map(int, input().split())
graph = defaultdict(set)

# 양방향 구현 (목표 지점, 비용)
for node in range(M):
    a, b, c = map(int, input().split())
    graph[a].add((b, c))
    graph[b].add((a, c))

# 비용 리스트 초기화(1번 노드부터 시작을 주의)
inf = int(1e9)
dist = [inf] * (N + 1)

# 다익스트라 구현
dijkstra()

# 정답
print(dist[N])
#====================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
1. 그냥 이차원 배열로 구현하는 다익스트라.

'''

'''
< 시간 복잡도 >
1. O((N + M) * logN)

'''

'''
< 문제 정리 >
1. 최소한의 소 + 경로
    -> 다익

2. 양방향 길.

3. 헛간: N, 소들의 길: M

4. A에서 B로 출발

5. 첫 번째 노드(1)에서 끝 노드(N)으로의 다익스트라
'''