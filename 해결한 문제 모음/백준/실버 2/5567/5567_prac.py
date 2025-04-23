import sys, time
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import defaultdict, deque

N = int(input())
E = int(input())
visited = [False] * (N + 1)

graph = defaultdict(set)
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].appned(a)

queue = deque()
queue.append([1])
ans = []
cnt = 0

visited[1] = True

while queue:
    arr = queue.popleft()

    temp = []

    for cur in arr:
        for child in graph[cur]:
            if visited[child]:
                continue
                
            visited[child] = True

            temp.append(child)

            ans.append(child)

    cnt += 1

    queue.append(temp)

print(len(ans))