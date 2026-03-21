import sys, time
start = time.time()
sys.stdin = open("input.txt")

#============================================
# < 함수 >: sv, sh, ev, eh를 받아서 해당 범위의 합을 구하는 함수.
def total_sum(sv, sh, ev, eh):
    ans = 0
    for v in range(sv, ev + 1):
        for h in range(sh, eh + 1):
            ans += grid[v][h]

    return ans

N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# sv, sh, ev, sh (시작이 0부터 시작하도록 조정).
nums = list()
for _ in range(M):
    sv, sh, ev, eh = map(int, sys.stdin.readline().split())
    print(total_sum(sv - 1, sh - 1, ev - 1, eh - 1))
#============================================

end = time.time()
print("time:", end-start)