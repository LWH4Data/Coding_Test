import sys
sys.stdin = open('input_2884.txt')

T = int(input())

for tc in range(1, T + 1):
    H, M = map(int, input().split())

    thr = M - 45


    if thr == 0:
        H = H - 1
        M = M - 45

        if H < 0:
            H = 23
            M = M


    if thr > 0:
        H = H
        M = M - 45

    if thr < 0:
        H = H - 1
        M = 60 + (M - 45)

        if H < 0:
            H = 23
            M = M

    print(H, M)