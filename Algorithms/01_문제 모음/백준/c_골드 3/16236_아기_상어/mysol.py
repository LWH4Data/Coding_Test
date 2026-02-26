import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#========================================================================
from collections import deque()

# 델타 로직
dv = (-1, 1, 0 ,0)
dh = (0, 0, -1, 1)

# < 함수 >: BFS 탐색
def BFS(v, h, dist):
    q = deque()
    visited = [[False] for _ in range(N)]
    q.append((v, h, dist))

# < 함수 >: 같은 크기의 수가 있는지 검증.
"""
해당 물고기를 기준으로 우측하단으로 graph를 탐색했을 때 같은 수가 없어야 함.
"""
def check_same(v: int , y: int) -> bool:
    pass

    # 위 아래 

# 입력값 받기.
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 상어의 위치 찾기.
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            v, h = i, j

# 상어의 위치에서 BFS를 수행해 가장 가까운 물고기 찾기. (이동 상태 저장, 큐에 넣을 때 +1).

    # 해당 물고기에 도착하였다면

        # 먹을 수 있는지

        # 여러 마리의 물고기가 있다면 예외
    
    # 남은 물고기가 있다면 다시 반복.

        # 없다면 종료.
        
#========================================================================

e_t = time.time()
print("time: ", e_t - s_t)