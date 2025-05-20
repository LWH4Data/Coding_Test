import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#====================================================================
from collections import defaultdict, deque

def topology():
    queue = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

            semester[i] += 1

    while queue:
        cur = queue.popleft()

        for child in graph[cur]:
            indegree[child] -= 1

            semester[child] = max(semester[child], semester[cur] + 1)

            if indegree[child] == 0:
                queue.append(child)

T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())
    graph = defaultdict(set)
    edges = list(map(int, input().split()))

    for i in range(E):
        graph[edges[i * 2]].add(edges[i * 2 + 1])

    indegree = [0] * (N + 1)
    for node in range(1, N + 1):
        for child in graph[node]:
            indegree[child] += 1

    semester = [0] * (N + 1)
    topology()
    print(f'#{tc} {max(semester)}')
#====================================================================

end_time = time.time()
print('time :', end_time - start_time)

# 7 OK