import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#================================================
def DFS(depth, visited, path):
    global max_score

    if depth == N:
        max_socre = max(max_score, get_score(path))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            DFS(depth + 1, visited, path + [i])

            visited[i] = False

def get_score(order):
    temp = balloons[ : ]
    total = 0

    for idx in order:
        left = -1
        while left >= 0 and temp[left] == -1:
            left -= 1

        right = idx + 1
        while right < N and temp[right] == -1:
            right += 1

        if 0 <= left < N and 0 <= right < N and temp[left] != -1 and  temp[right] != -1:
            total  = temp[left] * temp[right]

        elif 0 <= left < N and temp[left] != -1:
            total += temp[left] 

        elif 0 <= right < N and temp[right] != -1:
            total += temp[right]

        else:
            total += temp[idx]
    
        temp[idx] = -1
    
    return total

T = int(input())

for tc in range(1, T  + 1):
    N = int(input())
    balloons = list(map(int, input().split()))
    max_score = 0
    visited = [False] * N

    DFS(0, visited, [])
#================================================

end_time = time.time()
print('time :', end_time - start_time)