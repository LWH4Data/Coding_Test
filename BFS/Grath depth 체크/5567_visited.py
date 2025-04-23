import sys, time
sys.stdin = open('input_5567.txt')
start_time = time.time()

#================================================
from collections import defaultdict, deque

T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    E = int(input())
    ans = 0

    # 1. 그래프 구현
    # (리스트 컴프리헨션 없이 바로 받기)
    graph = defaultdict(set)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    # visited를 누적합으로 구현하여 depth 체크
    visited = [0] * (N + 1)

    # BFS 수행
    queue = deque()

    # 시작은 1번 노드
    queue.append(1)
    visited[1] = 1

    while queue:
        cur = queue.popleft()

        for neighbor in graph[cur]:
            
            # 방문 체크
            if visited[neighbor]:
                continue
            
            # queue에 추가
            queue.append(neighbor)

            # 이전 노드의 depth + 1
            visited[neighbor] = visited[cur] + 1

    # 1: 본인
    # 2: 친구
    # 3: 친구의 친구
    # '나'를 제외한 나머지 count
    # 즉 visited에서 depth = 2 ~ 3 까지만 count
    # (visited[1]이 본인이기에 i = 1인 경우를 생략)
    for i in range(2, N + 1):
        if 0 < visited[i] <= 3:
            ans += 1
    
    print(ans)
#================================================

end_time = time.time()
print('time :', end_time - start_time)