import sys, time
sys.stdin = open("input.txt")
start = time.time()

#======================================================
from collections import deque

# union과 find를 함수로 구현하고 입력값에 따라 수행한다.

# find 함수.
def find(a, node = 0):
     
    if graph[a] == a:
        node = a
    
    if graph[a] != a:
        find(graph[a], node)
        graph[a] = node

    return node

def union(a, b):
    if graph[a] != graph[b]:
        temp_a = find(a)
        temp_b = find(b)

        if temp_a < temp_b:
            graph[b] = graph[a]
        else:
            graph[a] = graph[b]    

# 입력 받기
# n = 노드의 수, m = 연산의 수
n, m = map(int, sys.stdin.readline().split())
# graph
graph = [False] * (n + 1)
for i in range(1, n + 1):
    graph[i] = i
# 연산 리스트
test = deque()
for i in range(m):
    test.append(list(map(int, sys.stdin.readline().split())))

while test:
    c, a, b, = test.popleft()

    if c == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("No")
#======================================================

end = time.time()
print("time: ", end - start)