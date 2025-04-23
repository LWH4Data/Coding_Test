import sys
sys.stdin = open('input_10250.txt')

T = int(input())

for tc in range(1, T + 1):
    H, W, N = map(int, input().split())
    # 방의 층과 호수
    level = 0
    num = 0
    
    # 몫만큼 우로 이동
    horizon = N // H + 1
    
    # 나머지 만큼 위로 이동
    vertical = N % H

    if vertical == 0:
        level = H
        horizon = N // H

    # 층과 호수 배정
    level = level + vertical
    num = num + horizon

    if 0 < num < 10:
        print(str(level) + "0" + str(num))
    
    else:
        print(str(level) + str(num))