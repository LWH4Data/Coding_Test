import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#===========================================================================
# << 함수 >> switch 함수
def seg_switch(a, b):
    tree[startNode + a - 1] = b
    num_list[a - 1] = b

    for i in range(1, treeHeight + 1):
        tree[(startNode + a - 1) // 2**i] = min(tree[(((startNode + a - 1) // 2**i) * 2)], tree[(((startNode + a - 1) // 2**i) * 2 + 1)])

# << 함수 >> seg_min
def seg_min(start_idx, end_idx):
    start_idx += startNode
    end_idx += startNode 
    result = sys.maxsize

    while end_idx >= start_idx:
        if start_idx % 2 == 1:
            result = min(result, tree[start_idx])
            start_idx += 1
        if end_idx % 2 == 0:
            result = min(result, tree[end_idx])
            end_idx -= 1
        
        start_idx //= 2
        end_idx //= 2
    return result

# 입력 받기
N = int(sys.stdin.readline())

# tree 구현
length = N
treeHeight = 0

while length != 0:
    length //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight + 1)
tree = [0] * treeSize
startNode = pow(2, treeHeight)
num_list = list(map(int, sys.stdin.readline().split()))

for i in range(startNode, startNode + N):
    tree[i] = num_list[i - startNode]

for i in range(startNode - 1, 0, -1):
    tree[i] = min(tree[2*i], tree[2*i + 1])

M = int(sys.stdin.readline())
check_list = []
for _ in range(M):
    check_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(M):
    if check_list[i][0] == 1:
        seg_switch(check_list[i][1], check_list[i][2])

    if check_list[i][0] == 2:
        ans = num_list.index(seg_min(0, N - 1))
        print(ans + 1)
#===========================================================================

e_t = time.time()
print("time: ", e_t - s_t)