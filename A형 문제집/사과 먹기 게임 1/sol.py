'''
< 특이 사항 - 소거법 시뮬 불가 >
- 현제 문제는 continue를 통한 '소거법'으로 시뮬이 불가.
- 소거법이 안 되는 경우는?
    - 조건 두 개가 '독립적'으로 다루어지는 경우 경우의 수가 네 개 이기 때문에 소거법이 불가하다.
'''

import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#=============================================================
from collections import deque

# 델타 로직 (우, 하, 좌, 상), 처음 바라보고 있는 방향이 우측이기 때문.
dv = (0, 1, 0, -1)
dh = (1, 0, -1, 0)

# 탐색 BFS
    # input: 현재 좌표와 목표 사과 좌표
    # output: 이번 회전 수, 현재 v, 현재 h, 현재 방향(d)
def BFS(cur_v, cur_h, cur_d, target_v, target_h):
    
    # 삼차원 visited를 사용.
    # (방향 정보를 마지막에 넣어야하기 때문)
    visited = [[[False] * 4 for _ in range(N)] for _ in range(N)]
    queue = deque()

    # (위치, 방향, 회전 수)를 초기 값으로 입력.
    queue.append((cur_v, cur_h, cur_d, 0)) 

    # 방문 체크
    visited[cur_v][cur_h][cur_d] = True

    # 탐색 시작
    while queue:
        v, h, d, turn = queue.popleft()

        # 목표 지점 도착하면 (회전 수, v, h, d)를 반환
        if (v, h) == (target_v, target_h):
            return (turn, v, h, d)
        
        # 두 가지 경로를 추가해야함.
            # 1. 직진을 먼저 하는 경로
            # 2. 우측 회전을 하는 경로.
        
        # 1. 직진
        # 직진을 위한 좌표 초기화
        nv = v + dv[d]
        nh = h + dh[d]

        # 범위 내에 들어오고, 직진한 적이 없다면 직진
        if 0 <= nv < N and 0 <= nh < N and not visited[nv][nh][d]:

            # 방문 체크
            visited[nv][nh][d] = True

            # queue에 append
            # 이때 '직진'만하고 '회전'은 없기 때문에 (nv, nh)만 변경됨.
            # appendleft: 회전 없이 직진만을 우선하는 경우가 '최소 회전'을 보장하기 때문에 
            # 직진 경로를 항상 우선 처리.
            queue.appendleft((nv, nh, d, turn))

        # 2. 회전
        # 회전 연산 수행: +1을 하여 회전을 가하고, 4로 나누어 방향을 결정.
        nd = (d + 1) % 4

        # 회전은 범위가 넘어갈 일이 없기 때문에 새로운 방향만 체크하면 됨.
        if not visited[v][h][nd]:

            # 방문 체크
            visited[v][h][nd] = True

            # queue에 append
            # 이동 없이 회전만 하기에 (nd, turn + 1)만 변경.
            queue.append((v, h, nd, turn + 1))

    # 아무 것도 없는 경우 0을 반환하여 total_turn에 더해지는 값이 없게 함.
    return 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 사과 위치를 반환 (사과 번호, v, h)
    apples = []
    for v in range(N):
        for h in range(N):
            if graph[v][h] != 0:
                apples.append((graph[v][h], v, h))
    
    # 번호 순 정렬
    apples = sorted(apples)

    # 게임 시작
    # 전체 회전 수
    total_turns = 0
    cur_v, cur_h, cur_d = 0, 0, 0 # (시작 v, 시작 h, 방향)

    for _, target_v, target_h in apples:
        turns, cur_v, cur_h, cur_d = BFS(cur_v, cur_h, cur_d, target_v, target_h)
        total_turns += turns
    
    print(f'#{tc} {total_turns}')
#=============================================================

end_time = time.time()
print('time :', end_time - start_time)