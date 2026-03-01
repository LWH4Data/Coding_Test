import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#========================================================================
from collections import deque

# 델타(동, 남, 서, 북)
dv = (0, 1, 0, -1)
dh = (1, 0, -1, 0)

# 입력
N = int(sys.stdin.readline())
graph = [[False] * N for _ in range(N)]

# 사과 정보 반영
num_apple = int(sys.stdin.readline())
for _ in range(num_apple):
    v, h = map(int, sys.stdin.readline().split())
    # 사과는 1, 1 index를 사용하기에 각각에 -1
    graph[v - 1][h - 1] = "apple"

# 방향 정보 저장
num_dir = int(sys.stdin.readline())
X = [0] * 10001
for _ in range(num_dir):
    t, d = sys.stdin.readline().split()
    X[int(t)] = d

# 시작 상태
sv, sh, sdir = 0, 0, 0
graph[sv][sh] = "bem"

# 뱀 몸통 정보 저장 리스트.
bem_list = deque([(sv, sh)])
# 전체 걸린 시간
total_second = 0

# 시뮬 시작
while True:
    # 1) 다음 칸 이동.
    nsv = sv + dv[sdir]
    nsh = sh + dh[sdir]

    # 2) 벽 충돌 확인.
    if nsv < 0 or nsv >= N or nsh < 0 or nsh >= N:
        break

    # 3) 몸통 충돌 확인.
    if graph[nsv][nsh] == "bem":
        # 이동하는 칸이 가장 마지막 꼬리인 경우 이동과 동시에 꼬리가 빠지기에 예외처리.
        tail_v, tail_h = bem_list[0]
        if (nsv, nsh) != (tail_v, tail_h):
            break
    
    # 4) 사과 여부 확인.
    is_apple = (graph[nsv][nsh] == "apple")

    # 5) 머리 이동
    sv, sh = nsv, nsh
    graph[sv][sh] = "bem"
    bem_list.append((sv, sh))

    # 6) 사과가 아니면 꼬리 제거
    if not is_apple:
        tv, th = bem_list.popleft()
        graph[tv][th] = False

    # 7) 1초 증가.
    total_second += 1

    # 8) 방향 전환.
    if X[total_second] == 'D':
        sdir = (sdir + 1) % 4
    elif X[total_second] == 'L':
        sdir = (sdir - 1) % 4

print(total_second + 1)
#========================================================================

e_t = time.time()
print("time: ", e_t - s_t)