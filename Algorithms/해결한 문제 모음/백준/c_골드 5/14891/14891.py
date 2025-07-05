import sys, time
from collections import deque
sys.stdin = open('input_14891.txt')

start_time = time.time()

T = int(input())

def rotation(r, d):
    if first[2] == second[7]: # 첫 번재와 두 번째 톱니의 극이 같은 경우.
        # 1 번 톱니만 회전하고 종료.
        if r == 1 and d == -1: # 반시계 회전
            val = first.popleft() # 첫 번째 값을 삭제하고
            first.append(val) # 첫 번째 값을 마지막에 붙여서 반 시계 구현.

    elif first[2] != second[7] and second[2] == third[7]:
        if r == 1 and d == -1: # 반시계 회전
            val = first.popleft() # 첫 번째 값을 삭제하고
            first.append(val) # 첫 번째 값을 마지막에 붙여서 반 시계 구현.
            
            # 두 번째 톱니는 시계방향 회전.
            val = second.pop(-1)
            second.appendleft(val)
    
    elif first[2] != second[7] and second[2] != third[7] and third[2] == fourth[7]:
        if r == 1 and d == -1: # 반시계 회전
            val = first.popleft() # 첫 번째 값을 삭제하고
            first.append(val) # 첫 번째 값을 마지막에 붙여서 반 시계 구현.
            
            # 두 번째 톱니는 시계방향 회전.
            val = second.pop(-1)
            second.appendleft(val)

            # 세 번째 톱니 회전
            val = third.popleft()
            third.append(val)

    elif first[2] != second[7] and second[2] != third[7] and third[2] != fourth[7]:
        if r == 1 and d == -1: # 반시계 회전
            val = first.popleft() # 첫 번째 값을 삭제하고
            first.append(val) # 첫 번째 값을 마지막에 붙여서 반 시계 구현.
            
            # 두 번째 톱니는 시계방향 회전.
            val = second.pop(-1)
            second.appendleft(val)

            # 세 번째 톱니 회전
            val = third.popleft()
            third.append(val)

            # 네 번째 톱니 회전
            val = fourth.pop(-1)
            fourth.appendleft(val)



for tc in range(1, 1 + T):
    # 문자열로 받았음을 주의
    # 조건 체크할 때.
    first = deque(list(map(str, input())))
    second = deque(list(map(str, input())))
    third = deque(list(map(str, input())))
    fourth = deque(list(map(str, input())))
    K = int(input())
    # [[회전 톱니 번호, 방향], [회전 톱니 번호, 방향]]
    rotate = [list(map(int, input().split())) for _ in range(K)]
    







    break




end_time = time.time()
print('time :', start_time - end_time)

'''
1. 톱니바퀴
    - 8 개의 톱니
    - 톱니는 N or S 극을 갖음.
        - S = 0
        - N = 1
    - 왼쪽부터 1 ~ 4 번 톱니.

2. 톱니를 K 번 회전.
    - 시계 or 반시계

3. 회전시킬 톱니 + 방향 결정
    - 같은 극인 경우 회전 X
    - 다른 극인 경우 '반대 방향 회전'

4. 톱니의 합
    - 1 번 톱니 12 방향 N : 0 / S : 1
    - 2 번 톱니 12 방향 N : 0 / S : 2
    - 3 번 N : 0 / S : 3
    - 4 번 N : 0 / S : 4

5. 톱니 맞닿은 부분.
    - 1 번의 3번 톱니 & 2 번의 7번 톱니
    - 2 번의 3번 톱니 & 3 번의 7번 톱니
    - 3 번의 3번 톱니 & 4 번의 7번 톱니
'''