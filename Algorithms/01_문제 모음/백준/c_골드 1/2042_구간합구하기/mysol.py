import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

# 리스트를 받아 세그먼트 트리를 만든다.

# 수를 바꾸는 처리.

# 구간합 구하기.
#==============================================================
# 숫자 변경 및 다시 분할 합 구하기=================================
def swich_num(switch_idx, b):

    # n 번째의 수는 n-1 idx이기에 연산식에 -1을 포함한다.
    #   e.g. 1번째 수는 1 + 2**k - 1 = 2**K
    seg_tree[switch_idx + 2**k - 1] = b

    # leafnode가 변경되었기에 다시 segment tree를 만든다.
    for i in range(2**k, len(seg_tree) - 1, 2):
        seg_tree[int(i / 2)] = seg_tree[i] + seg_tree[i + 1]

# 구간합 함수.===================================================
def part_sum(start_idx, end_idx):

    result = 0
    temp = 0

    # 구간합 로직
    while start_idx < end_idx:
        if start_idx % 2 == 1:
            result += seg_tree[start_idx]
            start_idx = int((start_idx + 1) / 2)
        else:
            start_idx = int(start_idx / 2)
        
        if end_idx % 2 == 0:
            result += seg_tree[end_idx]
            end_idx = (end_idx - 1) / 2
        else:
            end_idx = int(end_idx / 2)
    
    print(result)

# 세그먼트 트리를 구현한다.
N, M, K = map(int, sys.stdin.readline().split())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

# 세그먼트 트리를 구현할 k 구하기.
k = 0
while 2 ** k < len(nums):
    k += 1

# 세그먼트 트리구현
seg_tree = [0] * 2**(k + 1)
for i in range(N):
    seg_tree[2**k + i] = nums[i]

for i in range(2**k, len(seg_tree) - 1, 2):
    seg_tree[int(i / 2)] = seg_tree[i] + seg_tree[i + 1]

for _ in range(K + M):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        swich_num(b, c)
    else:
        b = b + 2**k - 1
        c = c + 2**k - 1
        part_sum(b, c)

# a에 따라 분기

    # 1인 경우 해당하는 리프노드의 수를 변경

    # 2인 경우 구간합을 구하기. (함수)
#==============================================================

e_t = time.time()
print("time: ", e_t - s_t)