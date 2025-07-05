import sys
sys.stdin = open('input_10871.txt')

A, X = map(int, input().split())
num = list(map(int, input().split()))
new_num = []

for i in range(A):
    if num[i] < X:
        new_num.append(num[i])

print(' '.join(map(str, new_num)))