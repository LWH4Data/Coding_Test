import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=====================================================================
# 델타로직
dv = [-1, 0, 1, 0]
dh = [0, 1, 0, -1]


# 입력값 받기
N, M = map(int, sys.stdin.readline().split())
v, h, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 입력을 반복
check = True
cnt = 0
while check:

    # 청소 되지 않았다면 청소
    if not visited[v][h]:
        visited[v][h] = True
        cnt += 1
    
    # 주변 탐색
    temp = False
    for i in range(4):
        nv = v + dv[i]
        nh = h + dh[i]

        # 청소되지 않은 빈 칸이 있는 경우.
        if not visited[nv][nh] and graph[nv][nh] != 1:
            
            # 반 시계 방향으로 회전
            d = (d - 1) % 4

            # 바라 보는 방향의 앞쪽 칸이 청소되지 않았다면 전진.
            if not visited[v + dv[d]][h + dh[d]] and graph[v + dv[d]][h + dh[d]] != 1:
                v = v + dv[d]
                h = h + dh[d]
                temp = True

    if temp:
        continue

    # 후진 가능하다면 후진
    if graph[v + dv[(d + 2) % 4]][h + dh[(d + 2) % 4]] != 1:
        v = v + dv[(d + 2) % 4]
        h = h + dh[(d + 2) % 4]
    
    # 아니라면 탐색 중지
    else:
        check = False

print(cnt)
#=====================================================================

e_t = time.time()
print("time: ", e_t - s_t)