import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==================================================================================
from collections import deque

# 이동 로직에서 사용하기 위한 델타를 생성한다.
dv = (-1, 1, 0, 0) # vertical
dh = (0, 0, -1, 1) # horizontal

# 한쪽으로 쭉 이동하는 이동 함수를 정의한다.============================
def move(v, h, dv, dh, graph):
    dist = 0

    while True:

        # 델타 이동
        nv, nh = v + dv, h + dh
        
        # 벽과 만난 경우
        if graph[nv][nh] == '#':
            # 더 진행할 수 없기에 현재 상태를 반환한다.
            return v, h, dist, False
        
        # 벽이 아닌 경우 이동한 위치로 상태를 업데이트 한다.
        v, h = nv, nh
        dist += 1

        # 이동한 곳이 구멍이라면 반환.
        if graph[v][h] == 'O':
            return v, h, dist, True
        
# 문제 해결 함수.====================================================
def sol():
    # 입력값 받기
    N, M = map(int, sys.stdin.readline().split())
    graph = [list(sys.stdin.readline().strip()) for _ in range(N)]

    # 붉은 공과 파란 공의 위치를 저장.
    for v in range(N):
        for h in range(M):
            if graph[v][h] == 'R':
                rv, rh = v, h
            elif graph[v][h] == 'B':
                bv, bh = v, h
    
    # BFS로 탐색
    q = deque()
    # 다음 상태를 결정하는 정보는 붉은 공의 위치와 푸른 공의 위치이기에 각 좌표를 q에 넣는다.
    q.append((rv, rh, bv, bh, 0))
    # visited는 붉은 공과 푸른 공의 좌표 조합으로 표현한다.
    visited = set()
    visited.add((rv, rh, bv, bh))

    while q:
        rv, rh, bv, bh, cnt = q.popleft()

        # cnt가 10을 넘는 경우는 더이상 탐색할 필요가 없기에 skip
        if cnt >= 10:
            continue
        
        # 델타 탐색
        for d in range(4):
            nrv, nrh, rdist, r_hole = move(rv, rh, dv[d], dh[d], graph)
            nbv, nbh, bdist, b_hole = move(bv, bh, dv[d], dh[d], graph)

            # 파란 공이 구멍에 빠졌다면 실패.
            if b_hole:
                continue

            # 빨간 공이 구멍에 빠졌다면 성공.
            #   ● BFS이기에 최소를 보장한다.
            if r_hole:
                return cnt + 1
            
            # 파란 공과 빨간 공이 겹친다면 더 많이 이동한 공을 한칸 뒤로 이동한다.
            if nrv == nbv and nrh == nbh:
                if rdist > bdist:
                    nrv -= dv[d]
                    nrh -= dh[d]
                else:
                    nbv -= dv[d]
                    nbh -= dh[d]
            
            # 방문 체크
            state = (nrv, nrh, nbv, nbh)
            
            # 방문하지 않은 경우
            if state not in visited:
                # 방문 체그한 뒤
                visited.add(state)
                # 다음 탐색에 넣는다.
                q.append((nrv, nrh, nbv, nbh, cnt + 1))
        
    # while의 출력이 없는 경우는 cnt가 모두 10 이상인 경우이기에 -1을 반환.
    return -1

print(sol())
#==================================================================================

e_t = time.time()
print("time: ", e_t - s_t)