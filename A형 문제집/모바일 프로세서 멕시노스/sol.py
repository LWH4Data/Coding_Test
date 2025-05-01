import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#===========================================================
# 델타 로직
dv = (-1, 1, 0, 0)
dh = (0, 0, -1, 1)

# 델타 탐색을 하는데 경로 길이도 고려해야 하기에 별도의 함수로 작성한다.
def can_connect(v, h, dir):
    
    # for loop은 함수 외부에서 돌고있고, dir은 0부터 3까지임.
    nv = v + dv[dir]
    nh = h + dh[dir]

    # 경로를 받기 위한 변수 초기화
    path = []

    # 탐색 범위가 넘어가지 않는 이상은 탐색 지속.
    while 0 <= nv < N and 0 <= nh < N:
        
        # 전선(2)이거나 다른 멕시노스 코어(1)이라면 경로가 안되기에 []을 반환
        if graph[nv][nh] != 0:
            return []

        # 막히는 경우가 아니라면 지속적으로 경로를 업데이트하고, 최종 경로를 반환
        path.append((nv, nh))
        nv += dv[dir]
        nh += dh[dir]
    
    # while을 모두 돌았다면 경로를 다 찾은 것이기에 경로를 return
    return path
        
# DFS 탐색 함수
def DFS(idx, connected, total_len):
    
    # 앞서 초기화한 최대 연결 수와 최소 길이를 전역변수로 활용
    global max_connected, min_total_len

    # idx는 전체 코어를 확인했나 확인하는 변수
    # 일단 탐색이 끝난 경우 두 변수를 초기화 하고 return 한다.
    if idx == len(core_list):

        # 연결된 갯수가 더 많은 경우를 탐색했다면 '최대 연결 수'와 '최소 전선 길이'를 저장한다.
        if connected > max_connected:
            max_connected = connected
            min_total_len = total_len

        # 만약 연결의 수가 같은 경우를 찾았다면, 더 짧은 전선 길이로 초기화
        elif connected == max_connected:
            min_total_len = min(min_total_len, total_len)
        return

    # 각 멕시노스 탐색 시작.
    v, h = core_list[idx]

    # 델타 탐색 시작
    for dir in range(4):

        # 델타 탐색 함수
        path = can_connect(v, h, dir)
        
        # 경로가 반환되지 않은 경우 이번 탐색을 넘김
        if not path:
            continue

        # 경로가 반환 됐다면 해당 경로를 모두 2로 초기화하여 전선을 표시해 줌.
        for nv, nh in path:
            graph[nv][nh] = 2

        # 이후 추가 탐색을 위해 DSF 호출
        DFS(idx + 1, connected + 1, total_len + len(path))

        # DFS를 나온 경우 설치되었던 전선을 다시 원래 상태로 복구
        for nv, nh in path:
            graph[nv][nh] = 0

    # 연결이 안되는 멕시노스도 있기에 구현.
    DFS(idx + 1, connected, total_len)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 가장자리를 제외한 위치에 존재하는 멕시노스의 위치를 탐색
    core_list = []
    for v in range(1, N - 1):
        for h in range(1, N - 1):
            if graph[v][h] == 1:
                core_list.append((v, h))

    # 함수 내에 전달할 '최대 전선 수' 변수와 '최소 길이' 변수를 초기화
    max_connected = 0
    min_total_len = float('inf')

    # 깊이 우선 탐색
    DFS(0, 0, 0)

    # 탐색 결과 반환
    print(f'#{tc} {max_connected} {min_total_len}')
#===========================================================

end_time = time.time()
print('time :', end_time - start_time)