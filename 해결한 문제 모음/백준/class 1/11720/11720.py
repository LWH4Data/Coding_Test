import sys
sys.stdin = open('input_11720.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = input()
    ans = 0

    for i in range(N):
        ans += int(numbers[i])
    
    print(ans)
