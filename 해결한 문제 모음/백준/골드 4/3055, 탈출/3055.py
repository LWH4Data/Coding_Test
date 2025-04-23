import sys
from collections import deque

sys.stdin = open('input_3055.txt')

T = int(input())

# 상하좌우 이동 방향 (델타 탐색)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, T + 1):
    R, C = map(int, input().split())
    board = [list(input().strip()) for _ in range(R)]  # 2D 맵

    water_q = deque()  # 물이 퍼지는 BFS 큐
    hedgehog_q = deque()  # 고슴도치 이동 BFS 큐
    visited = [[False] * C for _ in range(R)]  # 방문 여부

    # 초기 상태 설정
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'S':  # 고슴도치 위치 저장
                hedgehog_q.append((i, j, 0))  # (행, 열, 이동 횟수)
                visited[i][j] = True
            elif board[i][j] == '*':  # 물 위치 저장
                water_q.append((i, j))

    # BFS 탐색 시작
    while hedgehog_q:
        # 1️⃣ **먼저 물 확장**
        for _ in range(len(water_q)):  
            x, y = water_q.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < R and 0 <= ny < C:
                    if board[nx][ny] == '.':  # 빈 공간이면 물로 채움
                        board[nx][ny] = '*'
                        water_q.append((nx, ny))

        # 2️⃣ **고슴도치 이동**
        for _ in range(len(hedgehog_q)):  
            x, y, step = hedgehog_q.popleft()

            # 도착 지점이면 출력 후 종료
            if board[x][y] == 'D':
                print(f"#{tc} {step}")
                break

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                    if board[nx][ny] == '.' or board[nx][ny] == 'D':
                        visited[nx][ny] = True
                        hedgehog_q.append((nx, ny, step + 1))
        else:
            continue
        break  # 비버 굴에 도착하면 BFS 종료

    else:
        print(f"#{tc} KAKTUS")  # 탈출 불가능



'''
1. R 행 / C 열 

2. 표시 
    - . : 비어 있는 곳
    - * : 물이 차있는 곳
    - X : 돌
    - D : 비버 굴
    - S : 고슴도치의 위치

3. 고슴도치 델타 이동. (상, 하, 좌, 우)
    - 물로 차있는 구역 이동 불가.
    - 물이 찰 예정인 곳도 이동 불가.


4. 물의 델타 이동. (상, 하, 좌, 우)
    - 비버의 소굴로 이동 불가.

5. 물과 고슴도치는 돌 통과 X

6. 고슴도치가 비버 굴로 이동하기 위한 최소 시간
    - 만약 이동 불가하다면 KAKTUS 출력.

7. 전체 크기 50 x 50 = 2500으로 완탐가능.

'''