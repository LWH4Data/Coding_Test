import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#==============================================================
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

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    voters = list(map(int, input().split()))
    print()


#==============================================================

end_time = time.time()
print('time :', end_time - start_time)