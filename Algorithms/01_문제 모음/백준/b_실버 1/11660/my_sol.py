"""
< 시간 복잡도 >

"""

import sys, time
start = time.time()
sys.stdin = open("input.txt")

#=================================
T = int(sys.stdin.readline())

for tc in range(1, T + 1):
    n, m = map(int, sys.stdin.readline().split())
    A = [[0] * (n + 1)]
    D = [[0] * (n + 1) for _ in range(n + 1)]
    
    # 원본 이차열 배열 생성
    #   ● 패딩을 두어 0 번째 인덱스를 0으로 추가.
    for i in range(n):
        A_row = [0] + [int(x) for x in input().split()]
        A.append(A_row)

    print(A)
    break
 
    # 입력값을 받는다.

    # 누적합을 저장할 이차원 배열을 생성하고 누적합을 계산한다.
    #   ● 0 번째 값은 없기에 padding을 추가한다.
#=================================

end = time.time()
print("time:", end-start)