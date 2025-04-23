import sys, time
sys.stdin = open('input_14567.txt')
start_time = time.time()

#======================================================
from collections import defaultdict, deque

# 위상정렬
def topological_sort():
    result = [] # 위상정렬된 리스트 반환
    queue = deque()

    # 모든 노드를 순회하면서 진입차수가 0이라면 추가
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    # 위상 정렬 시작
    while queue:
        cur = queue.popleft()

        for child in graph[cur]:
            # 현재 노드를 방문 했다는 것은.
            # 해당 노드의 자식 노드의 진입 차수가 -1 된 것.
            in_degree[child] -= 1

            # '진입차수 == 0'이라면 queue에 추가.
            if in_degree[child] == 0:
                queue.append(child)

            # 학기 초기화
            # 자식 노드는 다음 학기에 수강할 것이기에 '+1'
            ans[child] = ans[cur] + 1
    
    # 학기 결과 반환
    return ans

T = int(input())

for tc in range(1, 1 + T):
    N, E = map(int, input().split()) # N: 노드의 수 / E: 간선의 수
    edges = [list(map(int, input().split())) for _ in range(E)]

    # defaultdict을 통핸 graph 구현
    # ('set()'으로 구현해보자)
    graph = defaultdict(set)
    for edge in range(E):
        # set()은 append가 아닌 add
        graph[edges[edge][0]].add(edges[edge][1])

    # 진입 차수 구현
    in_degree = [0] * (N + 1)
    # 노드를 순회하면서
    for node in range(1, N + 1):
        # 각 노드의 자식에 + 1
        for child in graph[node]:
            in_degree[child] += 1

    # 학기 구현 (정답)
    # 1부터 시작하는 이유는 최소 '한 학기'이기 때문.
    ans = [1] * (N + 1)

    # 탐색 
    topological_sort()
    print(*ans[1 : ])
#======================================================

end_time = time.time()
print('time :', end_time - start_time)


'''
1. 최대 일때만 ans 업데이트
2. set 말고 list 사용
'''