import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#================================================
def DFS(depth, path):
    global max_score

    if depth == N:
        max_score = max(max_score, get_score(path))
        return

def get_score(order):
    temp = balloons[ : ]

    for idx in order:
        left = idx -1

        while left >= 0 and temp[left] == -1:
            left -= 1
        
        right = idx + 1
        while right < N and temp[right] == -1:
            right += 1

        if 0 <= left < N and 0 <= right < N and temp[left] != -1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    balloons = list(map(int, input().split()))
    max_score = 0
    visited = [False] * N

    DFS(0, [])
#================================================

end_time = time.time()
print('time :', end_time - start_time)