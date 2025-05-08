import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#========================================================
from collections import defaultdict, deque
# 문제에서 작업의 병렬처리라는 시뮬은 heapq를 통해 구현된다.
import heapq

'''
< 위상정렬 cycle 확인 >
- 위상정렬은 in_degree를 통해 사이클을 확인한다.
- union_find는 무방향 그래프의 사이클을 판단할 때 사용한다.
'''
def has_cycle():
    # 순환을 확인하기 위해 in_degree
    # (1차원 배열의 복사라 얕은 복사가 가능.)
    temp_deg = in_degree[ : ]
    
    # 사이클 확인 탐색 로직
    queue = deque()
    # 진입차수가 0인 노드만 queue에 넣고 탐색
    for i in range(1, N + 1):
        if temp_deg[i] == 0:
            queue.append(i)

    # 사이클이 존재하면 모든 노드를 방문할 수 있어야 함.
    # 즉, 'visited의 총 합 == 노드의 수(N)'
    visited = 0
    
    # 탐색
    while queue:
        cur = queue.popleft()
        visited += 1

        # 탐색에 해당하는 node의 진입차수를 1 감소
        for child in graph[cur]:
            temp_deg[child] -= 1

            # 선수작업을 탐색하고 그 결과 진입차수가 0이 된 노드는 탐색 노드에 추가.
            if temp_deg[child] == 0:
                queue.append(child)
    
    # visited != N인 의미는 cycle이 존재한다는 의미.
    # 반환 자체는 True 혹은 False가 반환됨.
    return visited != N

# 김수석 조건 시뮬레이션\
def simulate(boosted_task = None): # 도움 받는 작업을 기록하기 위해 boosted_task 인자 사용
    
    # 시뮬레이션을 수행하기 위한 얕은 복사 
    temp_deg = in_degree[ : ]
    ready = []
    ongoing = []
    complete = [0] * (N + 1)

    for i in range(1, N + 1):
        if temp_deg[i] == 0:
            # 작업을 시작할 수 있는 node들을 ready에 넣어둔다.
            # start_time을 기준으로 정렬하여 진행한다.
            # 모든 task를 'start_time = 0'인 상태로 넣는다.
            heapq.heappush(ready, (0, i)) # (start_time, task)

    # 준비 중이거나 진행 중인 작업이 없다면 종료.
    # ready와 ongoing 두 개를 번갈아 가면수 수행하는 이유는 '병렬 수행'을 시뮬하기 위해서이다.
    while ready or ongoing:
        # 1. 준비 중인 작업
        while ready:
            # 탐색할 작업과 그 시간을 초기화
            start, task = heapq.heappop(ready)

            # 해당하는 작업의 수행 시간을 dur에 초기화
            dur = durations[task]

            # 현재 업무가 도움을 받는 업무이면서 1보다 큰 경우 김수석이 도움.
            # 아닌 경우에는 // 2를 하지않고 dur를 그대로 넘김.
            if task == boosted_task and dur > 1:
                dur //= 2

            # ready 상태에서 작업이 시작 되었기에 ongoing으로 넘어간다.
            # 추가로 time(0)에 dur(현재 task의 시간)
            heapq.heappush(ongoing, (start + dur, task))

        # 2. 진행 중인 작업  
        while ongoing:
            # (해당 작업의 끝 시간, 해당 작업)을 초기화 한다.
            end, finished = heapq.heappop(ongoing)
            
            # 끝난 시각을 complete의 끝난 작업에 해당하는 시간을 idx 초기화
            complete[finished] = end
            
            # 다음 작업들을 탐색하기 위해 순회
            for child in graph[finished]:
                # 탐색을 하는 노드에 해당하는 진입차수를 차감.
                temp_deg[child] -= 1

                # 만약 진입차수가 0이 되면 탐색을 시작할 노드이기에 ready에 추가.
                if temp_deg[child] == 0:
                    heapq.heappush(ready, (end, child))
    
    # 최대 수행 시간을 반환
    # 최대 수행 시간을 반환하는 이유는 풀이 부분에서 이를 통해 연산을 하기 때문.
    return max(complete)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 작업에 걸리는 시간을 저장하는 리스트
    durations = [0]
    graph = defaultdict(set)
    in_degree = [0] * (N + 1)

    # graph 구현
    # 1번 노드부터니 범위 체크 잘 해야한다.
    for node in range(1, N + 1):
        # 한줄씩 입력받기.
        data = list(map(int, input().split()))
        # 작업 시간 추가.
        durations.append(data[0])
        # 만약 선수작업이 있다면 추가.
        for parent in data[2 : ]:
            # 중복되지 않는 경우에만 graph에 추가.
            # defaultdict가 set이기에 중복 추가 되어도 되지만 시간 복잡도를 최적화하기 위함.
            if node not in graph[parent]:
                graph[parent].add(node)
                # 진입차수 구현
                in_degree[node] += 1

    # 업무를 완료할 수 없는 경우는 사이클이 있는 경우이다.
    # has_cycle() 함수의 결과 True가 반환되면 cycle이 있는 것이기에 -1을 반환
    if has_cycle():
        print(f"#{tc} -1")
        # -1을 출력하고 하단의 로직이 실행되는 것을 방지하기 위해 이번 test case를 skip
        continue

    # 사이클이 없다면 시뮬레이션 수행.
    # 우선 김수석이 돕지 않는 경우의 최대 수행 시간을 반환
    result = simulate()
    
    # 이후 n 번째 노드를 돕는 경우를 순회하며 최대 수행 시간을 반환
    for i in range(1, N + 1):
        # 김수석이 돕지 않은 경우 vs i 번째 노드를 돕는 경우
        result = min(result, simulate(boosted_task = i))

    print(f"#{tc} {result}")
#========================================================

end_time = time.time()
print('time :', end_time - start_time)