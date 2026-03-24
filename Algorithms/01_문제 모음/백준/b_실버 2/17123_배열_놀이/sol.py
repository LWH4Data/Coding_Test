"""
행과 열의 합만 다루도록 하는 정보 압축 문제
"""

import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==============================================================
T = int(sys.stdin.readline())

for _ in range(T):
    # 입력 받기
    N, M = map(int, sys.stdin.readline().split())

    # 행과 열의 합만 다루도록 정보 압축.
    row_sum = [0] * (N + 1)
    col_sum = [0] * (N + 1)

    # 행과 열의 합 계산.
    for i in range(1, N + 1):
        # 한 줄씩 받아서
        arr = list(map(int, sys.stdin.readline().split()))
        # 우선 행 누적합 처리
        row_sum[i] = sum(arr)

        # 열은 각 값을 하나씩 처리
        for j in range(1, N + 1):
            col_sum[j] += arr[j - 1]
    
    # 이후 업데이트 값 처리.
    for _ in range(M):
        r1, c1, r2, c2, v = map(int, sys.stdin.readline().split())

        # row_sum 누적합 처리를 위한 연산
        width = c2 - c1 + 1
        # col_sum 누적합 처리를 위한 연산.
        height = r2 - r1 + 1

        # row_sum에 맞게 한 번에 연산 처리.
        for r in range(r1, r2 + 1):
            row_sum[r] += width * v
        
        # col_sum에 맞게 한 번에 연산 처리.
        for c in range(c1, c2 + 1):
            col_sum[c] += height * v
    
    # 정답 출력
    print(*row_sum[1 : ])
    print(*col_sum[1 : ])
#==============================================================

e_t = time.time()
print("time: ", e_t - s_t)