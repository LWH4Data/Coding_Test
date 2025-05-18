import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#==============================================================
T = int(input())

for tc in range(1, T + 1):
    Ms, Ma = map(int, input().split())
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ms = Ms

    for i in range(L + 1):
        
        if i != 0:
            Ms += Ma

        check_arr = []
        count = [0] * N
        if i != L:
            for j in range(N):
                if arr[j][i] < arr[j][i + 1]:
                    profit = (arr[j][i + 1]-arr[j][i]) / arr[j][i + 1]
                    check_arr.append([profit, j])
                    check_arr.sort(reverse = True)

        for j in range(len(check_arr)):
            while Ms >= arr[check_arr[j][1]][i]:
                Ms -= arr[check_arr[j][1]][i]
                count[check_arr[j][1]] += 1
            
        for j in range(N):
            Ms += count[j] * arr[j][i + 1]
    
    ans = Ms - ms - Ma * L
    print(f'#{tc} {ans}')

#==============================================================

end_time = time.time()
print('time :', end_time - start_time)