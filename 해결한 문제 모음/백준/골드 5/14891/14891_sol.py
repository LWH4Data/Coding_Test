import sys, time
from collections import deque

sys.stdin = open('input_14891.txt')

start_time = time.time()

T = int(input())

# 톱니바퀴 회전 함수
def rotate(gear, direction):
    if direction == 1:  # 시계 방향
        gear.appendleft(gear.pop())
    else:  # 반시계 방향
        gear.append(gear.popleft())

# 톱니바퀴 연쇄 회전 함수
def rotation(gears, r, d):
    rotate_dir = [0] * 4  # 회전 여부 저장 (0: 회전 안함)
    rotate_dir[r - 1] = d  # 선택된 톱니바퀴 회전 방향 지정

    # 왼쪽 톱니바퀴들 확인
    for i in range(r - 1, 0, -1):
        if gears[i][6] != gears[i - 1][2]:  # 맞닿은 톱니 극이 다르면 회전
            rotate_dir[i - 1] = -rotate_dir[i]
        else:
            break  # 맞닿은 톱니 극이 같으면 회전하지 않음

    # 오른쪽 톱니바퀴들 확인
    for i in range(r - 1, 3):
        if gears[i][2] != gears[i + 1][6]:  # 맞닿은 톱니 극이 다르면 회전
            rotate_dir[i + 1] = -rotate_dir[i]
        else:
            break  # 맞닿은 톱니 극이 같으면 회전하지 않음

    # 회전 적용
    for i in range(4):
        if rotate_dir[i] != 0:
            rotate(gears[i], rotate_dir[i])

for tc in range(1, 1 + T):
    # 4개의 톱니바퀴 입력을 deque로 저장
    gears = [deque(map(str, input().strip())) for _ in range(4)]
    
    # 회전 횟수 입력
    K = int(input())
    
    # 회전 명령 실행
    for _ in range(K):
        r, d = map(int, input().split())
        rotation(gears, r, d)

    # 결과 출력: 12시 방향의 톱니 값 확인 (점수 계산)
    score = 0
    for i in range(4):
        if gears[i][0] == '1':  # 12시 방향이 S극('1')이면 점수 추가
            score += (2 ** i)

    print(f"#{tc} {score}")

end_time = time.time()
print('Execution Time:', end_time - start_time)
