import sys, time
sys.stdin = open('input_9204.txt')
start_time = time.time()

#==========================================================
from collections import deque, defaultdict

# 이동 델타
dv = (-1, -1, 1, 1)
dh = (-1, 1, -1, 1)

def sol(game):
    answer = []
    '''
    < 문자 관련 함수 >
    - chr: 아스키코드 (정수) -> 문자
    - ord: 문자 -> 아스키코드 (정수)
    - str: 데이터의 type을 string으로 변환.
    '''

    '''
    < 1. convert객체에 익명 함수를 변수로 초기화 >
    - 개인적으로 'col, row' 형식을 선호하는 편인데, 문제에서 'row, col' 형식을 요구하기 때문에
    - x[1]: row를 먼저 변환하고, x[0]:col을 이후 연산해서 반환한다.
    '''
    # e.g. covert = A, 3
    convert = lambda x : chr(x[1] + 65) + ' ' + str(8 - x[0])

    # 나는 게임을 하나씩 받아오기 때문에 for loop 필요 없음.
    '''
    < 구조 >
    - col: 위에서 부터 8로 시작함으로 역순임.
        - '8 - int(game[1])'을 통해 행렬 탐색에 사용할 수 있는 형식으로 변환
    - row: 문자를 아스키코드로 변환하는데 아스키코드가 idx처럼 사용될 수 있게 변환.
        -> 'ord('A') = 65'임. 
        -> 따라서 ord 변환을 하고 -65를 하면 'A: 0, B: 1, C: 2, ...' 형식으로 변환할 수 있음.
    '''
    start_point = (8 - int(game[1]), ord(game[0]) - 65)
    end_point = (8 - int(game[3]), ord(game[2]) - 65)

    queue = deque()
    '''
    < 2. queue에 전달하는 정보는 유동적 >
    - 지금은 (시작 위치, count, 경로)
    '''
    queue.append(start_point, 0, convert(start_point)) 
    
    visited = [[False] * 8 for _ in range(8)]
    visited[start_point[0], start_point[1]] = True
    ans = 'Impossible' # 기본값을 Impossible로 설정.

    while queue: 
        cur, count, path = queue.popleft()

        # 목적지에 도달한 경우 전체 시행 횟수와 경로 반환
        if cur == end_point:
            ans = str(count) + ' ' + path
            return ans

        # 대각선을 이동하며 탐색
        for d in range(4):
            next_v = start_point[0] + dv[d]
            next_h = start_point[1] + dh[d]

            # 범위 벗어나는 경우 처리
            if next_v < 0 or next_v >= 8 or next_h < 0 or next_h >= 8:
                break

            # 방문한 곳이라면 skip
            if visited[next_v][next_h]:
                continue
            
            # 아니면 방문 처리
            visited[next_v][next_h] = True

            '''
            < 3. 경로 탐색 >
            - 이러면 목적지까지의 전체 경로가 queue에 포함되어 있기에 후에 한 번에 확인할 수 있다.
            '''
            # queue에 추가.
            queue.append((next_v, next_h), count + 1, path + ' ' + convert((next_v, next_h)))

    answer.append(ans)
    return answer

        
T = int(input())

for tc in range(1, 1 + T):
    
    # 입력값을 받을 빈 리스트
    game = []

    # 입력값을 조각내서 받아옴.
    game.append(input().split())
    
    # 답을 구하는 함수 적용.
    result = sol(game)

#==========================================================

end_time = time.time()
print('time :', end_time - start_time)