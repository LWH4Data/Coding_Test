import sys, time 
sys.stdin = open('input_13913.txt')
start_time = time.time()

#==================================================
''' 
< 포인트 정리 >
1. BFS 경로 저장 및 반환
    - 경로를 전달할 때에는 append() 메서드를 사용하면 안된다.
        - append() 메서드는 return을 하지 않고, 객체의 상태를 변화시키기 때문이다.
    - 대신 + 연산자로 경로를 더하고, 이를 다시 초기화 해야한다.

2. 시간 복잡도를 줄이기 위한 백트래킹
    - 현재 문제는 경로를 '+'형식으로 더할 경우 노드마다 경로를 연산하게 되어 O(N^2)이 된다.
    - 따라서 백트레킹이 필요하다.
'''
from collections import deque

# 백트래킹 로직
# 현재 노드를 입력 받아 경로를 역추적한다.
def back_track(cur):

    # 경로 탐색 시작
    data = []

    # 역으로 경로를 추적
    # 따라서 현재 노드 초기화
    temp = cur

    # 탐색 종료까지의 횟수를 순회한다.
    for _ in range(visited[cur] + 1):

        # 현재 노드를 데이터에 추가.
        data.append(temp)

        # 현재 노드의 부모 노드를 temp로 초기화.
        temp = check[temp]
    
    # '자식 - 부모 - 조부모' 순이기에 역으로 출력
    print(' '.join(map(str, data[ : : -1])))

# 탐색 로직
def BFS():
    queue = deque()
    queue.append(N)

    while queue:
        cur = queue.popleft()

        # 동생을 만난 경우 백트래킹
        if cur == K:

            # 걸린 시간 출력
            print(visited[cur])

            # 경로를 역추적한 결과 출력
            back_track(cur)
            return
        
        # 아니라면 탐색
        # in을 통환 탐색이 가능함을 인지.
        for next in (cur - 1, cur + 1, cur * 2):

            # 범위 넘어가면 skip
            if next < 0 or next > 100000:
                continue

            # 방문했다면 skip
            if visited[next]:
                continue

            # 아니라면 방문체크하고
            visited[next] = visited[cur] + 1

            # queue에 추가
            queue.append(next)

            # 백트래킹을 위해 부모와 자식 인접리스트(check)초기화
            check[next] = cur

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    # 방문 체크 배열.
    # T/F가 아닌 이유는 동색을 찾기까지 걸린 시간을 반환받고 이를 기준으로 백트래킹을 하기 위함.
    visited = [0] * 100001

    # 백트래킹을 위해 부모와 자식을 체크하는 배열
    # 'idx: 다음 노드, value: 현재노드' 구조를 통해 다음 노드를 idx로 받아 현재노드를 구한다.
    # 이를 통해 경로를 역추적하는 배열.
    check = [0] * 100001

    BFS()
#==================================================

end_time = time.time()
print('time :', end_time - start_time)
