# 1. BFS에서 Depth를 활용해야 하는 경우
## 백준 5567 - 결혼식
### 1. temp에 각 depth 별 노드를 받아서 순회
- 원하는 시점(depth)에서 탐색을 끝낼 수 있기에 `시간 복잡도`를 줄일 수 있다.
- BFS 시뮬 문제에 적합하다.
```python
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
```

### 2. visited를 통해 depth 정보를 받기.
- 결국 BFS를 통한 `완전 탐색`을 하게 된다. (즉, 시간 복잡도).
- 단, visited만을 활용하기에 직관적이다.
- 가벼운 문제 혹은 거리, depth만 필요한 경우 사용하기도 한다.
```python
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
```