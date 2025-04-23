import sys
sys.stdin = open('input_3052.txt')

T = int(input())

for tc in range(1, T + 1):
    num = []
    ans_num = []
    for _ in range(10):
        num.append(int(input()))

    for i in range(10):
        ans_num.append(num[i] % 42)

    ans = len(list(set(ans_num)))
    print(ans)