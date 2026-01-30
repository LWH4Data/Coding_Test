import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==============================================================
# 입력값 받기
N, M = map(int, sys.stdin.readline().split())

# 최솟값을 반환하는 함수=========================================
def seg_min(start_idx, end_idx):
    start_idx += startNode
    end_idx += startNode
    # 최대값을 초기화하고 업데이트 하는 방식으로 활용.
    #   ● list를 생성하고 append한 뒤 마지막에 min()을 처리하는 건
    #     메모리 낭비가 된다.
    result = sys.maxsize
    
    while start_idx <= end_idx:
        if start_idx % 2 == 1:
            result = min(result, seg_tree[start_idx])
            start_idx += 1
        
        if end_idx % 2 == 0:
            result = min(result, seg_tree[end_idx])
            end_idx -= 1
        
        start_idx //= 2
        end_idx //= 2
    
    print(result)

# segment tree 구현============================================
length = N
treeHeight = 0
while length != 0:
    length //= 2
    treeHeight += 1

# leafnode들 구현
treeSize = pow(2, treeHeight + 1)
seg_tree = [sys.maxsize] * treeSize
startNode = treeSize // 2
for i in range(startNode, startNode + N):
    seg_tree[i] = int(sys.stdin.readline())

# 부모 노드의 값 채우기
for i in range(startNode - 1, 0, -1):
    seg_tree[i] = min(seg_tree[2*i], seg_tree[2*i + 1])

# 쌍이 주어졌을 때 최솟값을 반환한다.
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    seg_min(a, b)
#==============================================================

e_t = time.time()
print("time: ", e_t - s_t)