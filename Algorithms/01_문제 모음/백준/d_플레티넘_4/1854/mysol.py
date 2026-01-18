import sys, time
sys.stdin = open("input.txt")
start_t = time.time()

# 완전 탐색에 걸리는 시간 O(V + E) 251,000?
#=============================================================
# ● count 기반 풀이도 가능하다.
# ● 구하는 거리의 순서가 작은 순으로 나오기 때문에 k번째에 기록하는 로직.
from collections import defaultdict
import heapq

# 입력값 받기
n, m, k = map(int, sys.stdin.readline().split()) # n: 도시의 수, m: 간선의 수, k: k 번째 최소 간선
graph = defaultdict(list)
for _ in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append((end, weight)) # (자식 노드, 가중치)
dist = [sys.maxsize] * (n + 1)
count = [0] * (n + 1)
ans = [0] * (n + 1)
# print(graph)

# 탐색 로직 설정
q = []
heapq.heappush(q, (0, 1)) # (가중치, 시작 노드), 출력시 -1로 수정.
while q:
    now_dist, now_node = heapq.heappop(q)
    print(1)
    # 현재 특정 노드를 몇 번째 탐색하는 것인지 저장.
    count[now_node] += 1
    if count [now_node] == k:
        ans[now_node] = now_dist
    
    for child in graph[now_node]:
        temp = now_dist + child[1]
        if dist[child[0]] > temp:
            dist[child[0]] = temp
        heapq.heappush(q, (dist[child[0]], child[0]))

# 몇 번째 도착인지 count하는 list를 만든다.

# 해당 노드의 도착인 경우(e.g. 3번 노드는 count[3] == 3) 그 때의 거리를 ans list에 기록한다.

# 정답출력.

#=============================================================

end_t = time.time()
print("time: ", end_t, start_t)