import sys, time
sys.stdin = open('input_16236.txt')
start_time = time.time()

# 큐 설정을 위한 불러오기
from collections import deque

queue = deque()

# 델타 로직
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
# 탐색 시뮬 구현
def bfs(size):
    pass


T = int(input())

for tc in range(1, T + 1):
    # 완탐 + 시뮬 문제... 아찔해...
    N = int(input()) # 크기

    board = [list(map(int, input().split())) for _ in range(N)]

    # 아기 상어 시작 좌표 받기
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                x = i
                y = j
                break
    
    # 아기 상어 좌표와 크기
    queue.append((x, y, 2)) # 처음 크기는 2임.


    










end_time = time.time()
print("time :", end_time - start_time)

'''
1. N x N 정사각형임 (X)

2. 물고기 M 마리, 상어 1 마리

3. 아기 상어와 물고기는 모두 '크기'를 갖고 있음.

4. 아기상어 
    - 처음 크기 2
    - 상, 하, 좌, 우 (델타 탐색)
    - 자기보다 큰 물고기가 있는 경우 이동 불가.
        - 크기가 같은 물고기의 경우 이동 가능.
    - 자기보다 작은 물고기만 먹을 수 있음.
        - 크기가 같은 물고기는 먹을 수 없음.

5. 먹을 수 있는 물고기가 없다면 (자기보다 작은 물고기가 없다면) 종료

6. 먹을 수 있는 물고기가 한 마리 이상이면, 가장 가까운 물고기한테 감.

7. 이동과 동시에 물고기를 먹음.

8. 자기의 크기과 '같은 수'의 물고기를 먹으면 크기가 1 증가.

9. 9 는 아기상어 위치, 1 ~ 6은 물고기 크기.
'''