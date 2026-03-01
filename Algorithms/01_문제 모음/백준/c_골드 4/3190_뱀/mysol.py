import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#========================================================================
from collections import deque

# 델타 (동, 남, 서, 북)
dv = (0, 1, 0, -1) # 동 남 서 북
dh = (1, 0, -1, 0)

# 입력
N = int(sys.stdin.readline())
graph = [[False] * N for _ in range(N)]
num_apple = int(sys.stdin.readline())
apple_position = []
for _ in range(num_apple):
    temp_v, temp_h = map(int, sys.stdin.readline().split())
    graph[temp_v - 1][temp_h - 1] = "apple"
# 방향 정보
num_dir = int(sys.stdin.readline())
X = [0] * 10001
for _ in range(num_dir):
    idx, dir = sys.stdin.readline().split()
    X[int(idx)] = dir

# 시작 설정.
# 뱀의 위치
sv, sh, sdir = 0, 0, 0 
graph[sv][sh] = "bem"

# 전체 시간.
total_second = 0

# 뱀의 좌표로 몸통 관리.
bem_list= deque()
bem_list.append((sv, sh))

# 시뮬 시작.
while True:

    # 바라 보는 칸으로 한 칸 이동.
    # print("sh: ", sh, "sv: ", sv)
    nsv = sv + dv[sdir]
    nsh = sh + dh[sdir]
    # for row in graph:
    #     print(row)

    # 벽이거나 몸통인 경우 끝.
    # 범위
    # print("nsv: ", nsv, "nsh: ", nsh)
    # print("total_second: ", total_second)
    if nsv < 0 or nsv >= N or nsh < 0 or nsh >= N:
        break
    
    # 몸통
    if graph[nsv][nsh] == "bem":
        break

    # 사과가 있는 경우 이동.
    if graph[nsv][nsh] == "apple":
        # 이동
        sv, sh = nsv, nsh
        # 뱀 상태 반영
        graph[sv][sh] = "bem"
        # 뱀 몸에 추가.
        bem_list.append((sv, sh))
        # 하단의 로직은 skip
        total_second += 1
        # 방향 조정.
        if X[total_second] == 'D':
            sdir = (sdir + 1) % 4
        elif X[total_second] == 'L':
            sdir = (sdir - 1) % 4
        else:
            pass
        continue

    # 사과가 아닌경우 몸통 땡겨옴.
    if graph[nsv][nsh] != "apple":
        # 이동 
        sv, sh = nsv, nsh
        # 밤 상태 반영
        graph[sv][sh] = "bem"
        # 몸통에 추가.
        bem_list.append((sv, sh))
        # 꼬리 하나는 버리기.
        tv, th = bem_list.popleft()
        graph[tv][th] = False
        total_second += 1

        # 방향 조정.
        if X[total_second] == 'D':
            sdir = (sdir + 1) % 4
        elif X[total_second] == 'L':
            sdir = (sdir - 1) % 4
        else:
            pass


print(total_second + 1)
#========================================================================

e_t = time.time()
print("time: ", e_t - s_t)