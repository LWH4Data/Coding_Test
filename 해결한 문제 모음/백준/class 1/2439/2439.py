import sys
sys.stdin = open('input_2439.txt')

N = int(input())

for i in range(1, N + 1):
    print(' ' * (N-i) + "*" * i )