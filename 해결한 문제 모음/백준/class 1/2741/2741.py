import sys
sys.stdin = open('input_2741.txt')

N = int(input())
num = []

for i in range(N):
    num.append(i + 1)


print('\n'.join(map(str, num)))