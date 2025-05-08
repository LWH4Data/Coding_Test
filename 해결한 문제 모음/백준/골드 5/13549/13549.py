import sys, time
sys.stdin = open('input_13549.txt')
start_time = time.time()

#===========================================================
from collections import deque

N, K = map(int, input().split())
visited = [-1] * 100001
visited[N] += 1

queue = deque()
queue.append(N)

while queue:
    cur = queue.popleft()

    # 이동 로직 세 개
    for next in (cur + 1, cur - 1, cur * 2):

        # 범위 초과하면 처형
        if next < 0 or next > 100000:
            continue

        # 방문 했으면 처형
        if visited[next] != -1:
            continue

        # 단순 이동과 순간 이동의 cost가 다름.
        if next == 2*cur:
            queue.append(next)
            visited[next] = visited[cur]

        else:
            queue.append(next)
            visited[next] = visited[cur] + 1
print()
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