import sys, time
sys.stdin = open("input.txt")
start_t = time.time()

#================================================
N, M = map(int, sys.stdin.readline().split())
edges = []
for _ in range(M):
    edges.append(list(map(int, sys.stdin.readline().split())))
ans = [sys.maxsize] * (N + 1)
ans[1] = 0

for start, end, weight in edges:
    if ans[start] != sys.maxsize and ans[end] > ans[start] + weight:
        ans[end] = ans[start] + weight
ans1 = ans.copy()
# print(ans1)

for start, end, weight in edges:
    if ans[start] != sys.maxsize and ans[end] > ans[start] + weight:
        ans[end] = ans[start] + weight
# print(ans)

flag = False
for i in range(len(ans)):
    if ans[i] != ans1[i]:
        flag = True

if flag:
    print(-1)
else:
    for i in range(2, len(ans)):
        if ans[i] == sys.maxsize:
            print(-1)
        else:
            print(ans[i])
#================================================

end_t = time.time()
print("time: ", end_t - start_t)