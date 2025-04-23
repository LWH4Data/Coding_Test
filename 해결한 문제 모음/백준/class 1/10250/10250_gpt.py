import sys
sys.stdin = open('input_10250.txt')

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    # 층 계산 (나머지가 0이면 H층으로 설정)
    floor = N % H
    room_num = (N // H) + 1

    if floor == 0:  # 꼭대기 층 배정 시 보정
        floor = H
        room_num -= 1

    # 호수가 한 자리 수일 때 0을 붙여 두 자리로 맞춤
    print(f"{floor}{room_num:02d}")