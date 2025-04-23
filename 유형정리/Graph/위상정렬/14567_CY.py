from collections import deque, defaultdict

n, m = map(int, input().split())

n_prerequisites = defaultdict(int)
dic = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())
    dic[a].add(b)
    n_prerequisites[b] += 1

result = [0 for _ in range(n+1)]

term = 1

q = deque()
cur_term = set()
for i in range(1, n + 1):
    if i not in n_prerequisites or n_prerequisites[i] == 0:
        cur_term.add(i)
        result[i] = term
q.append(cur_term)

while q:
    cur_term = q.popleft()

    next_term = set()

    term += 1

    for cur_module in cur_term:
        for neighbor in dic[cur_module]:
            n_prerequisites[neighbor] -= 1
            if n_prerequisites[neighbor] == 0:
                next_term.add(neighbor)
                result[neighbor] = term

    if next_term:
        q.append(next_term)

print(" ".join(map(str, result[1:])))