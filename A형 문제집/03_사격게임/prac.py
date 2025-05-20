import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#================================================
def DFS(depth, path):
    global max_score

    if depth == N:
        max_score = max(max_score, get_score(path))
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            DFS(depth + 1, path + [i])

            visited[i] = False

def get_score(order):
    temp = balloons[ : ]
    total = 0

    for idx in order:

        left = idx - 1
        while left >= 0 and temp[left] == -1:
            left -= 1

        right = idx + 1
        while right < N and temp[right] == -1:
            right += 1

        if 0 <= left < N and 0 <= right < N:
            total += temp[left] * temp[right]

        elif 0 <= left < N:
            total += temp[left]

        elif 0 <= right < N:
            total += temp[right]

        else:
            total += temp[idx]

        temp[idx] = -1
    
    return total
        

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    balloons = list(map(int, input().split()))
    visited = [False] * N
    max_score = 0

    DFS(0, [])

    print(f'#{tc} {max_score}')
#================================================

end_time = time.time()
print('time :', end_time - start_time)

# OK!