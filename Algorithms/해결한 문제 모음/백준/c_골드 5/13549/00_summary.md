# 1. 정리.
## 1-1. 로직
- 다익스트라
    - 간선의 가중치가 0과 1이기에 BFS + DP로 푸는 것이 사실상 효율적. (단, 본인이 DP를 아직 못한다).
## 1-2. 시간 복잡도
- 각 노드와 노드마다의 간선을 지나기에 $E * N$
    - 그러나 간선의 수($E$)는 상수 3이기에 생략된다.
- heapq의 정렬로 인한 $logN$
$$O(NlogN)$$
## 1-3. 주의
- 다익스트라에서 일시적으로 cost를 받는 temp는 경로를 탐색하는 for loop 내부에 위치해야한다.
    - 이유는 개별 경로 탐색 시마다 cost가 별도로 초기화 되어야 하기 때문.
# 2. 내 풀이
```python
import sys, time
sys.stdin = open('input_13549.txt')
start_time = time.time()

#===========================================================
from collections import deque
import heapq

N, K = map(int, input().split())
dist = [int(1e9)] * 100001
dist[N] = 0

queue = []
heapq.heappush(queue, ((0, N)))

while queue:
    cost, cur = heapq.heappop(queue)


    if dist[cur] < cost:
        continue

    # 이동 로직 세 개
    for next in (cur + 1, cur - 1, cur * 2):

        # 범위 초과하면 처형
        if next < 0 or next > 100000:
            continue

        # 단순 이동과 순간 이동의 cost가 다름.
        temp = 0
        if next == 2 * cur:

            if dist[next] <= temp + cost:
                continue

            dist[next] = temp + cost
            heapq.heappush(queue, ((dist[next], next)))

        else:
            temp += 1
            if dist[next] <= temp + cost:
                continue

            dist[next] = temp + cost
            heapq.heappush(queue, ((dist[next], next)))

print(dist[K])
#===========================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
- 단순 다익스트라. 대신 도착 지점이 동생임.

- 가중치가 0, 1이라 BFS인가?

'''

'''
< 시간 복잡도 >
- 100,000을 간선 세 개로 탐색.

- O(100,000 * 3 * log100,000)
    -> O(NlogN)

'''

'''
< 문제 정리 >
1. 수빈이의 점 N / 동생의 점 K
    - N: 0이상 100,000 이하
    - K: 0이상 100,000 이하

2. 수빈이의 이동
    2-1. 걷기
    2-2. 순간이동.

3. 1초 후 이동
    3-1. X - 1
    3-2. X + 1
    3-3. 2 * X

4. 가장 빠른 '시간'
    - 시간이 cost인 dijkstra
'''
```