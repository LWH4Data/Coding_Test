import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=========================================================================
import copy
import sys
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
myMap = [[0 for j in range(M)] for i in range(N)]
visited = [[False for j in range(M)] for i in range(N)]

for i in range(N):
    myMap[i] = list(map(int, input().split()))

# 섬 번호
sNum = 1
# 모든 섬 정보 이중 리스트
sumlist = list([])
# 1개의 섬 정보 리스트
mlist = []

# 섬에 한 칸(노드)을 더해주는 함수
def addNode(i, j, queue):
    myMap[i][j] = sNum
    visited[i][j] = True
    temp = [i, j]
    mlist.append(temp)
    queue.append(temp)

# 탐색을 통해 섬의 정보를 저장
def BFS(i, j):
    queue = deque()
    mlist.clear()
    start = [i, j]
    queue.append(start)
    mlist.append(start)
    visited[i][j] = True
    myMap[i][j] = sNum

    while queue:
        r, c = queue.popleft()
        for d in range(4):
            tempR = dr[d]
            tempC = dc[d]
            while r + tempR >= 0 and r + tempR < N and c + tempC >= 0 and c + tempC < M:
                if not visited[r + tempR][c + tempC] and myMap[r + tempR][c + tempC] != 9:
                    addNode(r + tempR, c + tempC, queue)
                else:
                    break
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1
    
    return mlist

# 섬 구분 작업 수행
for i in range(N):
    for j in range(M):
        if myMap[i][j] != 0 and not visited[i][j]:
            # 깊은 복사로 해서 주소를 공유하지 않음.
            # BFS를 통해 하나의 섬의 정보를 가져옴.
            tempList = copy.deepcopy(BFS(i, j))
            sNum += 1
            # 새로운 섬 넘버링
            sumlist.append(tempList)

pq = PriorityQueue()

# 섬의 각 지점에서 만들 수 있는 모든 에지를 저장
for now in sumlist:
    # 한 개의 섬 정보
    for temp in now:
        r = temp[0]
        c = temp[1]
        now_S = myMap[r][c]
        # 네 방향 탐색 → 우선순위 큐에 에지 정보 저장
        for d in range(4):
            tempR = dr[d]
            tempC = dc[d]
            blength = 0
            while r + tempR >= 0 and r + tempR < N and c + tempC >= 0 and c + tempC < M:
                # 같은 섬이면 에지를 만들 수 없음.
                if myMap[r + tempR][c + tempC] == now_S:
                    break
                # 같은 섬도 아니고 바다도 아니면
                elif myMap[r + tempR][c + tempC] != 0:
                    # 다른 섬 → 길이가 1 초과일 때 에지로 추가.
                    if blength > 1:
                        pq.put((blength, now_S, myMap[r + tempR][c + tempC]))
                    break
                # 바다인 경우 다리의 길이 연장
                else: 
                    blength += 1
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1

# find 함수 구현
def find(a):
    if a == parent[a]:
        return addNode
    else:
        parent[a] = find(parent[a])
        return parent[a]

# union 함수 구현
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

# 자기 자신을 대표 노드로 초기화
parent = [0] * sNum
for i in range(len(parent)):
    parent[i] = i

useEdge = 0
result = 0

# 최소 신장 트리 알고리즘 수행
while pq.qsize() > 0:
    v, s, e = pq.get()
    # 연결해도 사이클이 생기지 않으면
    if find(s) != find(e):
        union(s, e)
        result += visited
        useEdge += 1

# sNum이 실제 섬의 수보다 1 크기 때문에 섬의 번호 표시를 위해 -2로 연산
if useEdge == sNum - 2:
    print(result)
else:
    print(-1)
#=========================================================================

e_t = time.time()
print("time: ", e_t - s_t)