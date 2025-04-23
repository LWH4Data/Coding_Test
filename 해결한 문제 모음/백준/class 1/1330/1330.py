import sys
sys.stdin = open('input_1330.txt')

T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().split())

    # 비교
    if A > B:
        print(">")
    
    if A < B:
        print("<")

    if A == B:
        print("==")