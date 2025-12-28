import sys, time
sys.stdin = open("input.txt")
start = time.time()

#=================================================
from collections import defaultdict

# 입력값 받기
V = int(sys.stdin.readline().strip())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(V)]

# 
graph = defaultdict(list)
for edge in edges:
    for i in range(1, len(edge), 2):
        if edge[i] == -1:
            break
        else:
            graph[edge[0]].append((edge[i], edge[i + 1]))
            graph[edge[i]].append((edge[0], edge[i + 1]))

# 가장 큰 가중치만 담은 리스트 생성
max_length = [0] * (V + 1)
for i in range(1, V + 1):
    max_length[i] = max(graph[i], key=lambda x: x[1])
print(max_length)

# 그래프를 defaultdict으로 구현

# 각 key에 대해서 내림차순 정렬

# 각 키를 순회하며 가장 큰 경우만 상태 업데이트
#=================================================

end = time.time()
print("time:", start - end)