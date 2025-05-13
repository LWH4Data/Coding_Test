import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#==============================================================
from collections import defaultdict

# union-find
def find(parent, x):
    # 부모와 자식이 같지 않은 경우는 지속해서 재귀를 호출함.
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    # 'parent[x] == x'인 경우는 x의 root임.
    # 따라서 호출을 정지하고, 해당 root를 지속적으로 반환함.
    return parent[x]

def union(parent, a, b):
    # a와 b의 root 찾기
    a = find(parent, a)
    b = find(parent, b)

    # 더 작은 쪽이 root가 되도록 설정.
    # 이는 정렬을 하여 트리 구조를 만들기 위함.
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def is_connected(group, graph):
    # group: [True, False, True, ...] (n 번째 노드(마을)이 그룹에 포함되는지)
    # graph: 인접리스트로 구현된 그래프

    # 1. group이 True인 노드만 모음.
    group_list = [i for i in range(N) if group[i]]

    # 2. 해당 그룹이 공집합(어떤 자치구도 속하지 않음)이라면 False를 반환.
    if not group_list:
        return False
    
    # 3. 각 노드의 부모를 '자기 자신'으로 초기화
    # 각 노드가 독립적으로 존재하는 하나의 집단이 된다.
    parent = [i for i in range(N)]

    # 4. 그룹으로 지정된 노드들을 순환하면서
    for u in group_list:

        # 실제로 좌표(연결)가 존재한다면 Union을 통해 연결한다.
        for v in graph[u]:
            if group[v]:
             union(parent, u, v)
    
    # 5. 첫 번째 노드를 기준으로 root를 찾는다.
    root = find(parent, group_list[0])

    # 6. 5에서 찾은 root를 기준으로 나머지 노드를 순회하며 연결을 검사
    # all(): 모두 True이거나 False이면 True를 반환한다.
    return all(find(parent, v) == root for v in group_list)

def solve(): 

    # 1. 이차원 배열을 순회하면서 graph 생성.
    graph = defaultdict(list)
    for v in range(N):
        for h in range(N):
            if arr[v][h] == 1:
                graph[v].append(h)
    
    # 2. 최소 유권자 차이를 저장할 변수
    min_diff = float('inf')

    # 3. 모든 가능한 지역구 분할(부분집합)을 비트마스크로 완전 탐색
    '''
    < 함수 정리 >
    1. <<: 비트시프트 연산자
        - e.g. 1 << N: 1을 N만큼 비트 시프트
            -> 00001, 00010, 00100, ...

    2. bool: i번째 비트가 1인지 확인하는 연산.
        - e.g. bool(13 & (1 << i))이고, i = 0
            -> bool(13 & 1)
            -> bool(1)
            -> True
    '''
    for bit in range(1, (1 << N) - 1):

        # bit가 1인 경우 groupA
        groupA = [bool(bit & (1 << i)) for i in range(N)]
        # 그 외 나머지는 groupB
        groupB = [not x for x in groupA]

        # 4. is_connecte 함수를 통해 두 그룹이 내부적으로 연결된 경우만 연산
        if is_connected(groupA, graph) and is_connected(groupB, graph):
            # groupA의 유권자 수 합
            sumA = sum(voters[i] for i in range(N) if groupA[i])
            # groupB의 유권자 수 합.
            sumB = sum(voters[i] for i in range(N) if groupB[i])

            # 차이를 계산하고 min_diff에 더 작은 차이로 값 초기화
            min_diff = min(min_diff, abs(sumA - sumB))

    # 5. 분할 결과가 있다면 min_diff를, 아니면 -1을 반환한다.
    return min_diff if min_diff != float('inf') else -1

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    voters = list(map(int, input().split()))
    print(f'#{tc} {solve()}')
#==============================================================

end_time = time.time()
print('time :', end_time - start_time)