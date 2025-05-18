import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#==========================================================
def simulate(start):
    graph_c = graph[ : ]
    pos = start

    while True:
        cnt = 1

        while True:

            left = pos - cnt
            right = pos + cnt
            
            left_check = False
            if 0 <= left < N:
                if graph_c[left] == 1:
                    left_check = True

            right_check = False
            if 0 <= right < N:
                if graph_c[right]:
                    right_check = True

            if left_check and right_check:
                return False
            
            if left_check:
                graph_c[left] = 0
                pos = left
                break

            if right_check:
                graph_c[right] = 0
                pos = right
                break

            if left < 0 and right >= N:
                return True
            
            cnt += 1

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = list(map(int, input().split()))

    M -= 1

    if simulate(M):
        print(f'#{tc} 0')
        continue

    found = False
    for d in range(1, N):
        for next in (M - d, M + d):
            if 0 <= next < N and simulate(next):
                print(f'#{tc} {d}')
                found = True
                break
        
        if found:
            break
    else: 
        print(f'#{tc} -1')
#=========================================================

end_time = time.time()
print('time :', end_time - start_time)

# 5