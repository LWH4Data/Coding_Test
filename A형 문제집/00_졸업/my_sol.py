import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#====================================================================
from collections import defaultdict, deque

# 위상정렬 탐삭
def BFS():

    queue = deque()

    # indegree == 0인 경우를 초반 탐색 값으로 넣기.
    for i in range(N):
        if indegree[i] == 0:
            queue.append((0, i))
            visited[i] = True

    while queue:
        cnt, start = queue.popleft()

        # 위상정렬 탐색
        for child in graph[start]:
            indegree[child] -= 1

            if indegree[child] == 0:
                queue.append((cnt + 1, child))
    
    return cnt

    

T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())

    graph = defaultdict(set)
    edges = list(map(int, input().split()))
    for i in range(E):
        graph[edges[2 * i]].add(edges[2 * i + 1])

    # 진입차수 설정
    indegree = [0] * (N + 1)
    for node in range(N):
        for child in graph[node]:
            indegree[child] += 1

    # 방문 체크
    visited = [False] * (N + 1)

    # 진입차수가 0인 노드부터 탐색을 시작해서 queue가 빌 때까지 하면됨.
    ans = BFS()

    print
    




#====================================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
- BFS + 위상정렬

'''

'''
< 시간 복잡도 >
- 모든 노드를 탐색하는 경우인 O(N)

'''

'''
< 문제 정리 >
1. 과목 V 개

2. 선수 과목 (같은 학기 X)
    -> 위상정렬

3. 졸업까지 최소 몇 학기?
    - 최소? BFS로 탐색을 돌리면 가능하려나?
    -> BFS를 하면 모든 선수과목과 그 하위 과목을 한 번에 queue에서 탐색할 수 있기에
'''