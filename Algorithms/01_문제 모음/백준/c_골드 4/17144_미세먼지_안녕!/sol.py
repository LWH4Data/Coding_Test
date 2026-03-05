import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=======================================================================
"""
- 동시에 graph 업데이트하는 동시 업데이트 방식을 활용한다.
  → 따라서 누적 연산값을 저장할 이차원 리스트를 활용한다.
- 순차적인 업데이트가 아니기에 BFS를 사용하지 않는다.
"""

from collections import deque

# 델타 로직
dv = (-1, 1, 0, 0)
dh = (0, 0, -1, 1)

# < 함수 >: 미세먼지 확산 (동시 업데이트: delta 누적)
def expand_dust():
    # graph로 전체 상태를 관리.
    global graph

    # 연산할 값을 누적 저장.
    delta = [[0] * C for _ in range(R)]

    for v in range(R):
        for h in range(C):
            # 먼지인 경우에만 확산
            if graph[v][h] > 0:
                # 확산될 값 초기화
                spread = graph[v][h] // 5
                # 확산불가하면 skip 
                if spread == 0:
                    continue
                
                # 확산 가능한 방향의 수
                num_expandable = 0
                for i in range(4):
                    nv = v + dv[i]
                    nh = h + dh[i]

                    # 범위 체크
                    if nv < 0 or nv >= R or nh < 0 or nh >= C:
                        continue
                    # 공기청정기라면 skip
                    if graph[nv][nh] == -1:
                        continue

                    # 주변 값 초기화
                    delta[nv][nh] += spread
                    num_expandable += 1
                
                # 해당 칸 업데이트
                delta[v][h] -= spread * num_expandable
    
    # delta를 한 번에 연산
    for v in range(R):
        for h in range(C):
            # 공기청정기가 아니면 연산
            if graph[v][h] != -1:
                graph[v][h] += delta[v][h]

# < 함수 >: 공기청정기 작동 (위: 반시계, 아래: 시계)
def active_machine(upper, lower):
    
    # grpah로 전체 상태 관리.
    global graph

    # --- 위쪽(upper) : 반시계 ---
    # 교환하면서 저장할 변수 초기화
    # 처음은 공기청정기에서 나오는 공기로 0으로 초기화한다.
    prev = 0

    # 1) upper 왼 → 오
    for h in range(1, C):
        temp = graph[upper][h]
        graph[upper][h] = prev
        # 마지막 값은 저장하여 다음 반복으로 양도
        prev = temp

    # 2) upper 오른쪽 하단 → 오른쪽 상단
    for v in range(upper - 1, -1, -1):
        temp = graph[v][C - 1]
        graph[v][C - 1] = prev
        # 마지막 값은 저장하여 다음 반복으로 양도
        prev = temp
    
    # 3) 상단 오른쪽 → 상단 왼쪽
    for h in range(C - 2, -1, -1):
        temp = graph[0][h]
        graph[0][h] = prev
        # 마지막 값은 저장하여 다음 반복으로 양도
        prev = temp
    
    # 4) 마지막 좌측 상단 → 좌측 하단(공기청정기)
    for v in range(1, upper):
        temp = graph[v][0]
        graph[v][0] = prev
    
    # 다시 공기청정기 위치 재확인
    graph[upper][0] = -1

    # --- 아래쪽 : 사계 ---
    # 1) lower 왼 → 오
    for h in range(1, C):
        temp = graph[lower][h]
        graph[lower][h] = prev
        prev = temp

    # 2) 오른쪽 위 → 오른쪽 아래
    for v in range(lower + 1, R):
        temp = graph[v][C - 1]
        graph[v][C - 1] = prev
        prev = temp
    
    # 3) 하단 우측 → 하단 좌측
    for h in range(C - 2, -1, -1):
        temp = graph[R - 1][h]
        graph[R - 1][h] = prev
        prev = temp
    
    # 4) 좌측 하단 → 좌측 상단 (공기청정기)
    for v in range(R - 2, lower, -1):
        temp = graph[v][0]
        graph[v][0] = prev
    
    graph[lower][0] = -1

# 입력
R, C, T = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 1번 열에서 공기청정기 위치 찾기 
machine = []
for i in range(R):
    if graph[i][0] == -1:
        machine.append(i)
# 머신을 기준으로 위의 영역과 아래의 영역을 분리
upper, lower = machine[0], machine[1]

# T초 동안의 시뮬레이션
for _ in range(T):
    expand_dust()
    active_machine(upper, lower)

# 남은 미세먼지 합
ans = 0
for v in range(R):
    for h in range(C):
        if graph[v][h] > 0:
            ans += graph[v][h]

print(ans)
#=======================================================================

e_t = time.time()
print("time: ", e_t - s_t)