import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=======================================================================
from collections import deque
import copy

# 델타 로직
dv = (-1, 1, 0, 0)
dh = (0, 0, -1, 1)

# < 함수 >: 미세먼지 확산
#   - BFS로 확산
#   - 먼지의 상태는 grpah에서 관리
def expand_dust(q: list, t: int) -> list:
    """
    q를 입력 받아 먼지 확산에 따라 graph를 전역적으로 상태를 변화시킴
    q로 확산하는 상태는 해당 초를 넘지 않음.
    """
    q = deque(copy.deepcopy(dust_list))
    
    while q:
        
        v, h, t = q.popleft()
        print(v, h, t)
        

        # t 시점이 현재 탐색을 넘으면 skip
        #   - 현재는 모든 로직을 수행하고 시간을 처리하기에 T + 1을 조건으로 한다.
        if t > T + 1:
            continue
        
        # 몇 개의 칸에 확장되는지 확인하는 변수.
        check_cell = 0
        update_cell = []

        for i in range(4):
            nv = v + dv[i]
            nh = h + dh[i]

            # 범위 넘으면 skip
            if nv < 0 or nv >= R or nh < 0 or nh >= C:
                continue

            # 공기 청정기 일 때도 skip
            if graph[nv][nh] == -1:
                continue
            
            # 남은 경우 주변 칸의 개수를 업데이트.
            check_cell += 1
            # 업데이트할 칸을 버퍼 해두고 후에 배치 없데이트.
            update_cell.append((nv, nh))

            # 방문 확인
            if visited[nv][nh]:
                continue
            visited[nv][nh] = True

            q.append((nv, nh, t + 1))
        
        # 업데이트 해야할 칸 일괄 업데이트
        print("update: ", update_cell)
        if check_cell > 0:
            around_val = graph[v][h] // 5
            for nv, nh in update_cell:
                graph[nv][nh] += around_val
            graph[v][h] = graph[v][h] - (around_val * check_cell)
        
        for row in graph:
            print(row)

    return graph

# < 함수 >: 공기청정기 작동.
def active_machine():
    pass

# 입력
R, C, T = map(int, sys.stdin.readline().split()) # R: vertical, C: horizontal, T: time
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]


# 먼지의 좌표를 q로 상태관리.
t = 0
dust_list = [] 
for i in range(R):
    for j in range(C):
        if graph[i][j] != 0 and graph[i][j] != -1:
            dust_list.append((i, j, t))

# T 초가 될 때까지 로직을 수행.
#   - T 시점 까지기에 T + 1까지 수행.
visited = [[False] * C for _ in range(R)]

# 초기 위치 방문 체크
for v, h, t in dust_list:
    visited[v][h] = True

graph = expand_dust(dust_list, t)


# while t != T + 1:

    # 미세 먼지 확장
    # expand_dust()

    # 1초 로직 수행 후 증가.
    # t += 1
#=======================================================================

e_t = time.time()
print("time: ", e_t - s_t)