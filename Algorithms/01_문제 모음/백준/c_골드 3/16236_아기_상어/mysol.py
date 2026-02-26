import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#========================================================================
from collections import deque

# 델타 로직
dv = (-1, 1, 0 ,0)
dh = (0, 0, -1, 1)

# < 함수 >: BFS 탐색==========================================================
def BFS(v: int, h: int, size: int, cnt: int, dist: int) -> tuple[int, int, int, int, int]:
    # 가장 가까우면서 첫 번째로 탐색할 물고기가 아님을 확인.
    is_first = False
    q = deque()
    visited = [[False] * N for _ in range(N + 1)]
    q.append((v, h, size, cnt, dist))

    while q:
        v, h, size, cnt, dist = q.popleft()

        for i in range(4):
            nv = v + dv[i]
            nh = h + dh[i]

            # 범위를 벗어나는 경우 skip
            if nv < 0 or nv >= N or nh < 0 or nh >= N:
                continue
                
            # 물고기를 만났는데 나보다 크다면 skip
            if graph[nv][nh] > size:
                continue

            # 크기가 작은 경우 먼저 먹어되는지 확인하기.
            if graph[nv][nh] < size:
                is_first = check_same(nv, nh)

                if is_first:
                    # 먹은 횟수 증가.
                    cnt += 1
                    # 만약 먹은 횟수가 상어의 크기 이상이라면 크기 증가 시키고 초기화.
                    if cnt >= size:
                        size += 1
                        cnt = 0
                    
                    # 먹었기에 0처리.
                    graph[nv][nh] = 0
                    
                    # 먹은 경우 해당 위치가 끝지점이기에 반환.
                    return nv, nh, size, cnt, dist + 1

            # 아닌 경우 q에 넣고 탐색을 지속.
            if visited[nv][nh]:
                continue
            visited[nv][nh] = True
            q.append((nv, nh, size, cnt, dist + 1))

# < 함수 >: 같은 크기의 수가 있는지 검증.========================================
def check_same(v: int , h: int) -> bool:
    
    # 해당 물고기가 가장 먼저 방문할 물고가기 아니라면 False를 반환.
    for i in range(0, v + 1):
        for j in range(0, h + 1):
            # 지금과 동일한 칸은 확인하지 않는다.
            if i == v and j == h:
                continue
            # 만약 같은 크기의 물고기가 있다면 False를 반환한다.
            if graph[i][j] == graph[v][h]:
                return False
    
    # 아니라면 True를 반환한다.
    return False

# 풀이=======================================================================
# 입력값 받기.
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 상어의 위치 찾기.
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            v, h = i, j

# 
print(BFS(v, h, 2, 0 ,0))
        
#========================================================================

e_t = time.time()
print("time: ", e_t - s_t)