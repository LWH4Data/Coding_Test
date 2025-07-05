import sys
sys.stdin = open('input_2475.txt')

num = list(map(int, input().split()))
num_list = []
for i in range(len(num)):
    num_list.append(num[i]**2)

# 제곱의 합
uni_num = sum(num_list)

# 10으로 나눈 나머지 (답)
ans = uni_num % 10
print(ans)