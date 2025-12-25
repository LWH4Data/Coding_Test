import sys, time
sys.stdin = open("input.txt")
start = time.time()

#===================================================
# 각 색종이 구현
def S1(x, y):
    graph[x][y] = False
def S2(x, y):
    for i in range(2):
        for j in range(2):
            graph[x + i][y + j] = 0
def S3(x, y):
    for i in range(3):
        for j in range(3):
            graph[x + i][y + j] = 0   
def S4(x, y):
    for i in range(4):
        for j in range(4):
            graph[x + i][y + j] = 0
def S5(x, y):
    for i in range(5):
        for j in range(5):
            graph[x + i][y + j] = 0 

# DSF
def DFS():

    # 각 색종이를 큰 순서대로 탐색
    # 이 방법을 쓰면 시작 위치 상태 업데이트가 안 된다.
    for i in range(5, 0, -1):
        if i == 1:
            S5

# 입력 받기
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
# 색종이 상태 (index가 각 색종이).
S = [0, 5, 5, 5, 5, 5]




#===================================================

end = time.time()
print("time:", start - end)

# 색종이 붙이기 - 17136
# 그리디
# DFS 탐색
# 각 색종이 상태 관리
# 그래프 상태관리.
# 시간 복잡도는 신경 안 써도 되는 수준.
