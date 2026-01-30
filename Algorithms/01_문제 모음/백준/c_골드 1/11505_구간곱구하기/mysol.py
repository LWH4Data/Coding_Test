# 해당 문제는 그냥 세그먼트 트리를 구현하면 시간 초과가 뜬다.
#   ● 큰 수의 연산을 포함하기에 구현할 때부터 나눗셈을 수행하여 수를 줄여야 한다.
#   ● 필요하다면 sys.stdin.buffer.readline을 통해 입출력 시간도 통제가 필요하다.

import sys
# 하단의 입력은 로컬에서 문제를 풀 때 input.txt 파일을 읽기 위함이며
# 시간을 관리하기 위해서는 sys.stdin.buffer.readline을 사용하는 것이 좋다.
# sys.stdin = open("input.txt")


# 문제에서 요구하는 나머지 상수 (모든 곱 연산은 이 값으로 나머지)
# 편하게 사용하기 위해 변수로 사용한다.
MOD = 1_000_000_007

# 세그먼트 트리
#=======================================================
# 구간 곱을 구하는 함수
def seg_mult(a, b):
    start_idx = a + startNode - 1
    end_idx = b + startNode - 1
    
    result = 1

    while end_idx >= start_idx:
        if start_idx % 2 == 1:
            # 곱한 뒤 바로 MOD로 줄여 큰 정수 연산 방지
            result = (result * seg_tree[start_idx]) % MOD
            start_idx += 1
        
        if end_idx % 2 == 0:
            # 곱한 뒤 바로 MOD로 줄여 큰 정수 연산 방지
            result = (result * seg_tree[end_idx]) % MOD
            end_idx -= 1
        
        start_idx //= 2
        end_idx //= 2
    
    outputs.append(str(result))

# 값을 변경하는 함수.
def seg_switch(a, b):

    # 세그먼트 트리에서의 위치 찾기
    a = startNode + a - 1
    # leaf node의 값 변경
    # 변경 값도 MOD로 줄여 저장
    seg_tree[a] = b % MOD
    # 부모 노드로 index 변경
    a //= 2

    # 변경한 leaf node에 해당하는 부모 노드를 전부 변경
    while a != 0:
        # 부모 노드도 MOD 적용
        seg_tree[a] = (seg_tree[2*a] * seg_tree[2*a + 1]) % MOD
        a //= 2

# 입력값 받기
# N: 수의 개수, M: 수의 변경 횟수, K: 구간 곱 횟수
# 빠른 입력을 위해 buffer 사용
input = sys.stdin.buffer.readline
N, M, K = map(int, input().split())
length = N

# 세그먼트 트리 구현
treeHeight = 0
# 트리의 높이 구하기
while length != 0:
    length //= 2
    treeHeight += 1

# 트리 리스트의 전체 길이 구하기
treeSize = pow(2, treeHeight + 1)
seg_tree = [1] * treeSize

# leaf node에 값 채워 넣기
startNode = treeSize // 2
for i in range(startNode, startNode + N):
    # 초기 값도 MOD 적용
    seg_tree[i] = int(input()) % MOD

# 나머지 부모 노드의 값 채워 넣기
for i in range(startNode - 1, 0, -1):
    # 초기 트리 구성 시에도 MOD 적용
    seg_tree[i] = (seg_tree[2*i] * seg_tree[2*i + 1]) % MOD

# 연산 수행
outputs = []  # 출력 버퍼에 모았다가 한 번에 출력
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        seg_switch(b, c)
    else:
        seg_mult(b, c)
#=======================================================
# 한 번에 출력해서 print 호출 비용 절감
sys.stdout.write("\n".join(outputs))