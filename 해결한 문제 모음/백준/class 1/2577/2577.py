import sys
sys.stdin = open('input_2577.txt')

A = int(input())
B = int(input())
C = int(input())

num = A * B * C
num = list(str(num))
ans_list = []

for i in range(10):
    cnt = 0
    for j in range(len(num)):
        if i == int(num[j]):
            cnt += 1
    ans_list.append(cnt)

print('\n'.join(map(str, ans_list)))