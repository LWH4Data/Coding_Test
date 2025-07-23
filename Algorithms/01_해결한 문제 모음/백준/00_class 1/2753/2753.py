
import sys
sys.stdin = open('input_2753.txt')

T = int(input())

for i in range(1, T + 1):
    N = int(input())

    if N % 4 == 0 and N % 100 != 0 or N % 400 == 0:
        print(1)

    else:
        print(0)