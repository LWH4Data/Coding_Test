import sys
sys.stdin = open('input_2920.txt')

T = int(input())

for tc in range(1, T + 1):
    pitch = list(map(int, input().split()))

    if pitch == [1, 2, 3, 4, 5, 6, 7, 8]:
        print("ascending")

    elif pitch == [8, 7, 6, 5, 4, 3, 2, 1]:
        print("descending")

    else:
        print("mixed")