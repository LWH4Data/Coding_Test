import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==========================================================
from collections import defaultdict

N = int(sys.stdin.readline())
tree = defaultdict(list)

for _ in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root].append((left, right))

print(tree['A'])
def preOrder(now):
    if now == '.':
        return
    # 1. 현재 노드
    print(now, end='')
    # 2. 왼쪽 탐색
    preOrder(tree[now][0])
    # 3. 오른쪽 탐색
    preOrder(tree[now][1])

def inOrder(now):
    if now == '.':
        return
    # 1. 왼쪽 탐색
    inOrder(tree[now][0])
    # 2. 현재 노드
    print(now, end='')
    # 3. 오른쪽 탐색
    inOrder(tree[now][1])

def postOrder(now):
    if now == '.':
        return
    # 1. 왼쪽 탐색
    postOrder(tree[now][0])
    # 2. 오른쪽 탐색
    postOrder(tree[now][1])
    # 3. 현재 노드
    print(now, end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
#==========================================================

e_t = time.time()
print("time: ", e_t - s_t)