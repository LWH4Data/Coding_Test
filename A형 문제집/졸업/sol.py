import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#====================================================================
from collections import defaultdict, deque

# 위상정렬
def topology():

    # 탐색 방법은 BFS
    queue = deque()

    for i in range(1, N + 1):

        # 진입차수가 0인 과목부터 시작
        if indegree[i] == 0:
            queue.append(i)

            # 진입차수가 0인 과목들은 1학기에 수강함을 가정.
            semester[i] = 1

    # 탐색 시작
    while queue:
        cur = queue.popleft()

        for child in graph[cur]:

            # 탐색한 노드는 진입차수를 하나씩 제거
            indegree[child] -= 1

            # 단, 학기는 더 오래 걸리는 학기를 선택.
            # 최대 학기 = 가장 긴 path = 모든 과목 수강 조건 충족.
            semester[child] = max(semester[child], semester[cur] + 1)

            # 진입차수가 0인 노드가 생겼다면 다음 탐색 대상.
            if indegree[child] == 0:
                queue.append(child)
        
T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())

    # 그래프 구현
    graph = defaultdict(set)
    edges = list(map(int, input().split()))
    for i in range(E):
        graph[edges[2 * i]].add(edges[2 * i + 1])

    # 진입차수 구현
    indegree = [0] * (N + 1)
    for node in range(1, N + 1):
        for child in graph[node]:
            indegree[child] += 1

    # 정답을 위한 시뮬
    semester = [0] * (N + 1)
    topology()
    print(f"#{tc} {max(semester)}")
#====================================================================

end_time = time.time()
print('time :', end_time - start_time)