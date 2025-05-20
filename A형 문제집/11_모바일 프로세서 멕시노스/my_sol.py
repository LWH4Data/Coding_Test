import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#===================================================
def DFS(num):
    
    # 탐색 범위 넘어가면 return
    if num >= len(m_position):
        return

    # 탐색하는 멕시노스의 좌표를 받는다.
    v, h = m_position[num][0], m_position[num][1]

    # 상, 우, 하, 좌를 탐색하며 연결한다.
    for dir in range(4):
        check = False

        if dir == 0:
            
            # 위쪽 방향을 보면서 
            for nv in range(0, v):
                
                # 멕시노스가 있거나 전선(2)이면 skip
                if graph[nv][h] == 1 or graph[nv][h] == 2:
                    check = True
                    break
            
            if check:
                continue
            
            else:
                # 전선 체크
                for nv in range(0, v):
                    graph[nv][h] = 2
                
                # 추가 탐색
                DFS(num + 1)

                # 끝나고 나오면 되돌리기
                for nv in range(0, v):
                    graph[nv][h] = 0

        if dir == 1:
            
            # 오른쪽 방향을 보면서 
            for nh in range(h + 1, N):
                
                # 멕시노스가 있거나 전선(2)이면 skip
                if graph[v][nh] == 1 or graph[v][nh] == 2:
                    check = True
                    break
            
            if check:
                continue
            
            else:
                for nh in range(h + 1, N):
                    graph[v][nh] = 2
                
                DFS(num + 1)

                for nv in range(0, v):
                    graph[nv][h] = 0
                
        if dir == 2:

            # 아래 방향
            for nv in range(v + 1, N):
                if graph[v][nh] == 1 or graph[v][nh] == 2:
                    check = True
                    break

            if check:
                continue
            
            else:
                for nv in range(v + 1, N):
                    graph[nv][h] = 2
                
                DFS(num + 1)

                for nv in range(0, v):
                    graph[nv][h] = 0
        
        if dir == 3:

            # 좌측 방향
            for nh in range(0, h):
                if graph[v][nh] == 1 or graph[v][nh] == 2:
                    check = True
                    break

            if check:
                continue
            
            else:
                for nh in range(0, h):
                    graph[v][nh] = 2
                
                DFS(num + 1)

                for nh in range(0, h):
                    graph[v][nh] = 0
        
    

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 우선 모든 멕시노스 좌표를 튜플로 받음.
    # 이때 가장자리 좌표는 반환받지 않음을 주의해야 한다.
    m_position = []
    for v in range(1, N - 1):
        for h in range(1, N - 1):
            if graph[v][h] == 1:
                m_position.append((v, h))
    
    # DFS로 구현
    DFS(0)



#===================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 변수 명세 >
- m_positionk: 멕시노스의 좌표 리스트

'''

'''
< 로직 1 >
1. 가장 자리에 있는 멕시노스를 제외한 나머지 멕시노스의 좌표를 받는다.

2. 각 멕시노스 마다 상, 하, 좌, 우 가능한 곳으로 직선 경로로 전선을 연결한다.
    e.g. 첫 번째 멕시노스 위로 연결
    -> 두 번째 멕시노스도 위로 연결
    -> 전선이 겹친다면 첫 번째 멕시노스를 우로 연결하고 
    -> 두 번째 멕시노스는 그대로 위로 연결
    -> 가능한 경우의 전선 길이를 tuple에 append하고
    -> 반환

3. 멕시노스의 수가 12개라 DFS가 가능할 듯한데??


1. 완전 탐색을 돌리거나.

2. 그리디 거나

3. 시뮬 문제 같은데.

'''

'''
< 시간 복잡도 >
- 최악의 경우 모든 경로를 고려하니까 O(N^2)을 넘을리 없다.

- 따라서 O(12 * 12)

- 완탐 가능.
'''

'''
< 문제 정리 >

'''