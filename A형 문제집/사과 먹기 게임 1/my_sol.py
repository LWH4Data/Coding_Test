import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#=====================================================
# 방향 및 이동로직
dir = (0, 1, 2, 3) # 우, 하, 좌, 상
dv = (0, 1, 0, -1)
dh = (1, 0, -1, 0)



def find_apple(v, h):
    
    # 회전 횟수 변수를 0으로 초기확
    trun_cnt = 0

    

    # 해당 위치에서 상, 우, 하, 좌로 사과있나 확인

    # 있다면 해당 방향으로 회전 or 전진

    # 없다면 보는 방향으로 한 칸 이동.

    # 위 행동 반복.
    
    # 시작 위치 start를 현재 위치로 초기화

    # retrun은 몇 번 회전했는지.

    

T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 리스트로 사과의 값과 위치 반환
    # (n 번째 사과, v, h)
    apple = []

    for v in range(N):
        for h in range(N):
            if graph[v][h]:
                apple.append((graph[v][h], v, h))
    
    # 순서대로 사과를 찾기위해 정렬
    apple = sorted(apple)

    # while이나 for loop으로 돌아야 할 것 같긴한데
    # while을 사용.
    # 전체 탐색 횟수는 사과의 갯수
    flag = len(apple)

    # cnt를 늘려가며 whiule 순회 종료 시점 기록
    cnt = 0

    # 시작 위치 초기화 (0, 0, 0) = (dir(우측), v, h)
    start = [0, 0, 0]

    while cnt < flag:

        a, v, h = apple[cnt]

        # 좌표를 받아 해당 사과 위치까지 이동하며 회전 횟수를 카운트하는 함수.
        find_apple(v, h)

        # cnt 1증가
        cnt += 1
    
    break


#=====================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
1. 사과의 위치를 list로 반환 받는다.

2. 좌측위에서 출발하고, 바라보는 쪽으로만 이동하면서 BFS로 상, 하, 좌, 우 사과 있나 확인.

3. 사과 잇다면 방향을 바구고 해당 지점으로 지직.
'''

'''
< 시간 복잡도 >
1. N이 최대 10, 사과의 수가 최대 10이기에 10 * 10 * 10 = 1000 
    -> 완탐가능.
'''

'''
< 문제 정의 >
1. 그래프 크기 N * N

2. 오른쪽으로만 회전 가능.
'''