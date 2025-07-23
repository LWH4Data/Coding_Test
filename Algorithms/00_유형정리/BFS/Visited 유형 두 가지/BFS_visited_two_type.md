# BFS의 두 가지 visited 방식
## 백준 1012 - 유기농 배추
- BFS에서는 방문 처리를 할 때 두 가지 방식 중 하나를 선택할 수 있다.
    1. queue.popleft() 직후
    2. queue.append() 직전
- 코드
```python
# 1. queue.popleft() 직후
while queue:
    v, h = queue.popleft()

    '''
    1. queue에서 pop하자마자 방문 처리 후 확인.
        - 직관적임.
    '''
    if visited[v][h]:
        continue
    visited[v][h] = True

# 2. queue.append() 직전
    # idx 명칭이 다른 것을 주의해야한다. (델타 탐색 중이기 때문)
if visited[nv][nh]:
    continue
visited[nv][nh] = True
queue.append((nv, nh))
'''
```
## 1. 먼저 방문처리
```python
import sys, time
sys.stdin = open('input_1012.txt')
start_time = time.time()

#============================================================================
from collections import deque

# 델타로직 생성
dv = (-1, 1, 0, 0) # 상, 하, 좌, 우
dh = (0, 0, -1, 1)

# BFS함수
def BFS(init_i, init_j):
    queue = deque()
    queue.append((init_j, init_i))
    
    # 탐색 시작
    while queue:
        v, h = queue.popleft()

        '''
        1. queue에서 pop하자마자 방문 처리 후 확인.
          - 직관적임.
        '''
        if visited[v][h]:
            continue
        visited[v][h] = True

        # 델타 순환
        for k in range(4):
            nv = v + dv[k]
            nh = h + dh[k]

            # 조건 확인
            # 조건은 '소거법'으로 하면 안되는 것들만 한 줄로 넣어주는 게 좋음.
            if nv < 0 or nv >= N or nh < 0 or nh >= M:
                continue

            if not graph[nv][nh]:
                continue

            if visited[nv][nh]:
                continue
            
            queue.append((nv, nh))
    
    return 1

T = int(input())

for tc in range(1, T + 1):
    M, N, K = map(int, input().split()) # M: 가로 / N: 세로 / K: 배추 좌표
    graph = [[0] * M for _ in range(N)]
    queue = deque()
    visited = [[False] * M for _ in range(N)]
    ans = 0

    # 좌표를 받으면서 graph 구현
    for i in range(K):
        h, v = map(int, input().split()) 
        graph[v][h] = 1

    # 모든 영역에 대해서 BFS를 수행
    for i in range(M):
        for j in range(N):
            # 0인 경우는 배추지역이 아니니 탐색 안해도 됨.
            if graph[j][i] == 0:
                continue

            # 방문한 곳도 탐색 안함.
            if visited[j][i] == True:
                continue

            ans += BFS(i, j)
    
    print(ans)
```

## 2. 뒤에서 방문처리
- append하기 전에 처리하기에 `탐색 속도`와 `메모리`가 소폭 최적화 됨.
```python
import sys, time
sys.stdin = open('input_1012.txt')
start_time = time.time()

#============================================================================
from collections import deque

# 델타로직 생성
dv = (-1, 1, 0, 0) # 상, 하, 좌, 우
dh = (0, 0, -1, 1)

# BFS함수
def BFS(init_i, init_j):
    queue = deque()
    queue.append((init_j, init_i))
    
    # 탐색 시작
    while queue:
        v, h = queue.popleft()

        # 방문한 곳이면 탐색이 필요 없기에 반환
        if visited[v][h]:
            continue
        visited[v][h] = True

        # 델타 순환
        for k in range(4):
            nv = v + dv[k]
            nh = h + dh[k]

            # 조건 확인
            # 조건은 '소거법'으로 하면 안되는 것들만 한 줄로 넣어주는 게 좋음.
            if nv < 0 or nv >= N or nh < 0 or nh >= M:
                continue

            if not graph[nv][nh]:
                continue

            if visited[nv][nh]:
                continue
            visited[nv][nh] = True
            queue.append((nv, nh))
            '''
            1. queue에 append를 한 뒤에 방문체크
              - 위에서 설명한 것과 같은 이점을 갖음.
            '''
            
    return 1

T = int(input())

for tc in range(1, T + 1):
    M, N, K = map(int, input().split()) # M: 가로 / N: 세로 / K: 배추 좌표
    graph = [[0] * M for _ in range(N)]
    queue = deque()
    visited = [[False] * M for _ in range(N)]
    ans = 0

    # 좌표를 받으면서 graph 구현
    for i in range(K):
        h, v = map(int, input().split()) 
        graph[v][h] = 1

    # 모든 영역에 대해서 BFS를 수행
    for i in range(M):
        for j in range(N):
            # 0인 경우는 배추지역이 아니니 탐색 안해도 됨.
            if graph[j][i] == 0:
                continue

            # 방문한 곳도 탐색 안함.
            if visited[j][i] == True:
                continue

            ans += BFS(i, j)
    
    print(ans)
```