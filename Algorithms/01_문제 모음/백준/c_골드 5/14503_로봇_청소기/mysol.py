import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=====================================================================
# 방향에 맞는 델타 로직
dv = (-1, 0, 1, 0)
dh = (0, 1, 0, -1)

# 입력값 받기
N, M = map(int, sys.stdin.readline().split())
v, h, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 청소 로직 실행
check = True
cnt = 0
while check:

    # 현재 칸이 청소되지 않은 칸이면 청소.
    if not visited[v][h]:
        visited[v][h] = True 
        cnt += 1

    # 청소되지 않은 빈 칸이 있는 경우.
    three = False
    for i in range(4):
        nv = v + dv[i]
        nh = h + dh[i]

        if 0 <= nv < N and 0 <= nh < M and not visited[nv][nh] and graph[nv][nh] == 0:
            three = True
            
            # 반시계로 회전했을 때 앞이 전진 가능한 만큼 반복
            temp = 0
            while temp != 4:
                # 반시계로 90도 회전
                d = (d - 1) % 4

                # 바라 보는 칸이 청소되지 않은 빈 칸이면 전진
                if not visited[v + dv[d]][h + dh[d]] and graph[v + dv[d]][h + dh[d]] == 0:
                    v = v + dv[d]
                    h = h + dh[d]
                    # 종료
                    temp  = 4
                # 아니라면 한 번 더 회전
                else:
                    temp += 1
            break

    # 청소되지 않은 빈 칸이 없는 경우.
    if not three:

        # 후진이 가능하다면 후진
        if graph[v + dv[(d + 2) % 4]][h + dh[(d + 2) % 4]] == 0:
            v = v + dv[(d + 2) % 4]
            h = h + dh[(d + 2) % 4]
        # 불가하다면 종료
        else:
            check = False

print(cnt)
#=====================================================================

e_t = time.time()
print("time: ", e_t - s_t)