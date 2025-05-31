import sys
sys.stdin = open('input_1152.txt')

T = int(input())

for tc in range(1, T + 1):
    words = list(input().split())
    ans = len(words)
    print(ans)