import sys
sys.stdin = open('input_27866.txt')

T = int(input())

for i in range(1, T + 1):
    word = input()
    num = int(input())

    ans = word[num - 1]
    print(ans)