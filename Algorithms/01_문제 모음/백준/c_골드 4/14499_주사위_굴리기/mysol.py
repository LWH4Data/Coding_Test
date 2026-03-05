import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=================================================================
import copy

# < 함수: 주사위 이동 >=============================================
def move_dice(dice: list, dir: int) -> list:
    """
    주사위의 상태, 이동 방향을 입력으로 받은 뒤
    다음 주사위의 상태를 반환한다.
    """

    # 이동 로직은 동, 서, 북, 남 네 개
    #   - 이중 리스트가 아니기에 얕은 복사
    temp_dice = dice.copy()
    
    # 동쪽
    if dir == 1:
        dice[1] = temp_dice[3]
        dice[3] = temp_dice[6]
        dice[4] = temp_dice[1]
        dice[6] = temp_dice[4]

    # 남쪽
    if dir == 4:
        dice[1] = temp_dice[2]
        dice[2] = temp_dice[6]
        dice[5] = temp_dice[1]
        dice[6] = temp_dice[5]
    
    # 서쪽
    if dir == 2:
        dice[1] = temp_dice[4]
        dice[3] = temp_dice[1]
        dice[4] = temp_dice[6]
        dice[6] = temp_dice[3]
    
    # 북쪽
    if dir == 3:
        dice[1] = temp_dice[5]
        dice[2] = temp_dice[1]
        dice[5] = temp_dice[6]
        dice[6] = temp_dice[2]
    
    return dice
        

# 델타: 동, 서, 북, 남 반시계 방향
# 1 ~ 4로 이동 로직이 주어지기에 0을 추가.
dv = (0, 0, 0, -1, 1)
dh = (0, 1, -1, 0, 0)

# 입력
# N: 새로 크기, M: 가로 크기, v: vertical, h: horizontal, K: 굴리는 명령
N, M, v, h, K = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
directs = list(map(int, sys.stdin.readline().split()))
# 주사위의 상태: [0, 'u', 'b', 'r', 'l', 'f', 'd']
dice = [0, 0, 0, 0, 0, 0, 0]

# 시뮬레이션 실행.
for dir in directs:

    # 범위 확인.
    if v + dv[dir] < 0 or v + dv[dir] >= N or h + dh[dir] < 0 or h + dh[dir] >= M:
        continue

    # 주사위 위치부터 이동.
    v, h = v + dv[dir], h + dh[dir]

    # 이동한 위치의 숫자 반영.
    dice = move_dice(dice, dir)

    # 해당 위치의 숫자가 0인 경우
    if graph[v][h] == 0:
        # 그래프에 숫자 주사위 숫자 복사
        graph[v][h] = dice[6]

    # 0이 아닌 경우
    else:
        # 칸의 숫자를 주사위에 복사
        dice[6] = graph[v][h]
        # 해당 칸은 0으로 초기화.
        graph[v][h] = 0
    
    print(dice[1])    
#=================================================================

e_t = time.time()
print("time: ", e_t - s_t)