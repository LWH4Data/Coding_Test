import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#==========================================================
def simulate(start):
    graph_c = graph[ : ]
    pos = start

    while True:
        # 탐색 거리 단위는 1
        cnt = 1

        while True:
            
            # 좌, 우 탐색위치 초기화
            # 탐색 범위는 누적합(혹은 차)로 구현한다.
            left = pos - cnt
            right = pos + cnt

            # 왼쪽 보석 확인.
            left_check = False
            if 0 <= left < N:
                if graph_c[left] == 1:
                    left_check = True

            # 오른쪽 보석 확인.
            right_check = False
            if 0 <= right < N:
                if graph_c[right] == 1:
                    right_check = True

            # 양쪽에 보석이 존재하는 경우 중지
            if left_check and right_check:
                return False
            
            # 한쪽만 있는 경우 해당 위치로 이동
            if left_check:

                # 이동한 위치의 보석은 이미 얻은 것이므로 0 처리.
                graph_c[left] = 0

                # 위치 초기화
                pos = left
                break
            
            # 왼쪽의 경우와 동일.
            if right_check:
                graph_c[right] = 0
                pos = right
                break

            # 양쪽 다 없는 경우
            if left < 0 and right >= N:
                return True
            
            # 해당 위치에서 탐색하지 못하였기에 다음 거리를 탐색.
            cnt += 1

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = list(map(int, input().split()))

    # M의 시작은 1인데 python에서 idx의 시작이 0이기에 1을 차감하여 맞춰준다.
    M -= 1

    # M에서 시작하는 경우를 따로 고려.
    if simulate(M):
        print(f"#{tc} 0")
        continue

    # M에서 한 칸씩 멀어지면서 탐색.
    # 가능한 경우가 없는 경우를 고려.
    found = False
    for d in range(1, N):
        for next in (M - d, M + d):

            # 탐색 범위가 graph 내에 있고, 전체 탐색이 되는 경우 거리(d) 출력
            if 0 <= next < N and simulate(next):
                print(f"#{tc} {d}")
                found = True
                break

        # 가능한 경우가 있다면 탐색 종료    
        if found:
            break
    
    # 가능한 경우가 없는 경우 -1을 반환
    else:
        print(f"#{tc} -1")
#==========================================================

end_time = time.time()
print('time :', end_time - start_time)

