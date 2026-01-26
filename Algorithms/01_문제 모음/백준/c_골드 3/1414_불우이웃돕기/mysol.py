import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

# 기부이기에 랜선의 총합에서 MST 결과를 뺀다.
# ● N == 1일 때의 엣지 케이스가 하나 있다.
#=============================================================
from collections import defaultdict
import heapq

# 로직에서 사용할 a-z, A-Z 문자와 수치 매핑 list
char_list = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# 입력 받기
N = int(sys.stdin.readline())
grid_graph = [list(sys.stdin.readline().strip()) for _ in range(N)]

# grid_graph의 문자를 숫자로 변환.
for i in range(N):
    for j in range(N):
        if grid_graph[i][j] == '0':
            grid_graph[i][j] = 0
        
        grid_graph[i][j] = char_list.index(grid_graph[i][j])

if N == 1:
    print(grid_graph[0][0])
else:

    # 총합 구하기
    total_sum = 0
    for row in grid_graph:
        total_sum += sum(row)

    # grid_graph를 통해서 graph 생성.
    graph = defaultdict(list)
    for i in range(N):
        for j in range(N):
            
            if grid_graph[i][j] != 0:
                graph[i].append((j, grid_graph[i][j]))
                graph[j].append((i, grid_graph[i][j]))

    # Prim 알고리즘 준비
    q = []
    heapq.heappush(q, (0, 1))
    visited = [False] * N
    result = 0

    while q:
        now_weight, now_node = heapq.heappop(q)
        if visited[now_node]:
            continue
        visited[now_node] = True

        result += now_weight
        
        for next_node, next_weight in graph[now_node]:
            if visited[next_node]:
                continue
            heapq.heappush(q, (next_weight, next_node))

    # 전체를 방문했는지 체크
    check = False
    for i in visited:
        if not i:
            check = True

    # 출력부 구현.
    if check:
        print(-1)
    elif N == 1:
        print(grid_graph[i][j])
    else:
        print(total_sum - result)
#=============================================================

e_t = time.time()
print("time: ", e_t - s_t)