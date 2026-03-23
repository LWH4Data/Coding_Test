import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==============================================================
T = int(sys.stdin.readline())

# M * M 구간의 범위의 합을 구하는 함수.
def grid_sum(sv: int, sh: int) -> int:
    """
    구간의 좌측위 좌표를 받아 구간합을 구한다.
    """
    total_sum = 0

    for i in range(sv, sv + M):
        for j in range(sh, sh + M):
            total_sum += grid[i][j]
    
    return total_sum

for tc in range(1, T + 1):
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    ans = 0

    # 전체를 순회하면서 가장 큰 값을 찾기.
    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            ans = max(grid_sum(i, j), ans)
    print(f"#{tc}", ans)
#==============================================================

e_t = time.time()
print("time: ", e_t - s_t)