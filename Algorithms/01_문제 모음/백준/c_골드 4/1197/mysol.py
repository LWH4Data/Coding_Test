import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==================================================================

# find 함수
def find(a):
    if parent[a] == a:
        return a
    
    while a != parent[a]:
        a = parent[a]
        parent[a] = a
    return a

# union 함수
def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

N, E = map(int, sys.stdin.readline().split())
edges = []
for _ in range(E):
    edges.append(list(map(int, sys.stdin.readline().split())))
edges = sorted(edges, key=lambda x: x[2])
parent = [0] * (N + 1)
for i in range(N + 1):
    parent[i] = i

ans = 0
check = 0
c = 0
while c != N - 1:
    s, e, w = edges[check]
    if find(s) == find(e):
        check += 1
    else:
        union(s, e)
        check += 1
        c += 1
        ans += w

print(ans)
#==================================================================

e_t = time.time()
print("time: ", e_t - s_t)