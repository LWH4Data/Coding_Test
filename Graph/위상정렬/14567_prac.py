from collections import defaultdict, deque

def topological_sort():
    result = []
    queue = deque()

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        cur = queue.popleft()

        for child in graph[cur]:
            in_degree[child] -= 1

            if in_degree[child] == 0:
                queue.append(child)

            ans[child] = ans[cur] + 1

T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    graph = defaultdict(set)
    for edge in range(E):
        graph[edges[edge][0].append(edges[edge][1])]

    in_degree = [0] * (N + 1)
    for node in range(1, N + 1):
        for child in graph[node]:
            in_degree[child] += 1

    ans = [1] * (N + 1)