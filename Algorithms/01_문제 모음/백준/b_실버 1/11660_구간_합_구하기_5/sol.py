import sys, time
start = time.time()
sys.stdin = open("input.txt")

#============================================
"""
이차원 리스트의 누적합을 활용한 풀이.
"""
# < 함수 >: sv, sh, ev, eh의 범위 정보를 받아서 합을 구하는 함수.
def total_sum(sv, sh, ev ,eh):
    return prefix[ev + 1][eh + 1] - prefix[sv][eh + 1] - prefix[ev + 1][sh] + prefix[sv][sh]
# 입력값 받기
N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# grid의 좌상단부터 우하단까지 누적합을 저장하는 prefix 이차원 리스트 초기화.
# - 누적합을 구할 때 가장자리가 포함되면 항상 예외처리가 필요하기에 이를 제거하기 위해
#   prefix는 1-index를 사용한다.
prefix = [[0] * (N + 1) for _ in range(N + 1)]
# prefix의 값을 채운다.
for v in range(1, N + 1):
    for h in range(1, N + 1):
        # 위와 좌측의 누적합 영역을 더하고, 중복되는 영역을 제거한 뒤, 추가되는 한 칸(prefix[v][h]의 단일 값 = grid[v - 1][h - 1])을 더함.
        # grid[v - 1][h - 1]: prefix의 1-index를 grid의 0-index로 치환한 값이다.
        # prefix[v - 1][h]: 하나 위의 행에 해당하는 누적합 영역
        # prefix[v][h - 1]: 하나 좌측에 해당하는 열의 누적합 영역
        # prefix[v - 1][h - 1]: 좌측 상단까지의 누적합 영역
        prefix[v][h] = grid[v - 1][h - 1] + prefix[v - 1][h] + prefix[v][h - 1] - prefix[v - 1][h - 1]

# 총 M 개의 결과를 반환.
for _ in range(M):
    sv, sh, ev, eh = map(int, sys.stdin.readline().split())
    print(total_sum(sv - 1, sh - 1, ev - 1, eh - 1))
#============================================

end = time.time()
print("time:", end-start)