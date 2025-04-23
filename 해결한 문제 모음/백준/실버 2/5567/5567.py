import sys, time
sys.stdin = open('input_5567.txt')
start_time = time.time()

#=======================================================
from collections import defaultdict,deque

# BFS 탐색 로직
def BFS(node):
    queue = deque()
    queue.append(node)
    ans = []
    ans.append(node)
    cnt = 0

    # 방문 체크
    visited[node] = 1

    # 탐색 시작
    while queue:

        cur = queue.popleft()

        for child in graph[cur]:
            
            # 방문 체크
            if visited[child]:
                continue

            # 아니라면 체크
            visited[child] = 1

            # queue에 삽입
            if cnt < 3:
                queue.append(child)

            # 정답에도 삽입.
            ans.append(child)

        # 탐색 횟수 초기화
        cnt += 1
    
    return len(ans)

T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    E = int(input())
    edges = [list(map(int, input().split())) for _ in range(E)]
    visited = [0] * (N + 1)
    res = 0

    # defaultdict로 graph 구현 (양방향임)
    graph = defaultdict(set)
    for edge in range(E):
        graph[edges[edge][0]].add(edges[edge][1])
        graph[edges[edge][1]].add(edges[edge][0])

    res = BFS(1)
    if not res:
        print(0)
    else:
        print(res)
#=======================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 문제 해석 >
1. 동기는 N명

2. 동기는 1부터 N까지 (2, N + 1)

3. 시작 노드 1

4. BFS를 돌리고 포함되는 모든 노드의 수 - 1
    4-1. 상근이를 제외해야 하기에 1을 뺀다.

5. 친구의 친구 즉, 두 번 BFS를 수행하겠다.
'''