import sys, time
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import defaultdict, deque

N = int(input())
E = int(input())
visited = [False] * (N + 1)
res = 0

# defaultdict로 graph 구현 (양방향임)
graph = defaultdict(set)
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

queue = deque()
queue.append([1])
ans = []
cnt = 0

# 방문 체크
visited[1] = True

# 탐색 시작
while cnt < 2:
    arr = queue.popleft()

    temp = []

    for cur in arr:
        for child in graph[cur]:
            # 방문 체크
            if visited[child]:
                continue

            # 아니라면 체크
            visited[child] = True

            # queue에 삽입
            temp.append(child)

            # 정답에도 삽입.
            ans.append(child)

    # 탐색 횟수 초기화
    cnt += 1
    queue.append(temp)

print(len(ans))