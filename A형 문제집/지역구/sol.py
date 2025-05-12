import sys
from collections import defaultdict
sys.stdin = open('sample_in.txt')
input = sys.stdin.readline

# 유니온 파인드
def find(x, parent):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y, parent):
    x_root = find(x, parent)
    y_root = find(y, parent)
    if x_root != y_root:
        parent[y_root] = x_root

def is_connected(group, graph, N):
    group_list = [i for i in range(N) if group[i]]
    if not group_list:
        return False

    parent = [i for i in range(N)]
    for u in group_list:
        for v in graph[u]:
            if group[v]:  # 같은 그룹 안에 있을 때만 union
                union(u, v, parent)

    root = find(group_list[0], parent)
    return all(find(v, parent) == root for v in group_list)

def solve(N, arr, voters):
    graph = defaultdict(list)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                graph[i].append(j)

    min_diff = float('inf')

    # 모든 가능한 지역구 조합 (비트마스크)
    for bit in range(1, (1 << N) - 1):
        groupA = [bool(bit & (1 << i)) for i in range(N)]
        groupB = [not x for x in groupA]

        if is_connected(groupA, graph, N) and is_connected(groupB, graph, N):
            sumA = sum(voters[i] for i in range(N) if groupA[i])
            sumB = sum(voters[i] for i in range(N) if groupB[i])
            min_diff = min(min_diff, abs(sumA - sumB))

    return min_diff if min_diff != float('inf') else -1

# 전체 입력 처리
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    voters = list(map(int, input().split()))
    print(f'#{tc} {solve(N, arr, voters)}')
