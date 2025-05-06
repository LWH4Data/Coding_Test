import sys, time
sys.stdin = open('input_4485.txt')
start_time = time.time()

#====================================================
# 다익스트라를 구현하기 위한 우선순위 큐 활용.
import heapq

# 델타 로직
dv = (-1, 1, 0 , 0)
dh = (0 ,0 , -1, 1)
# 1e9가 float type이기에 int 적용.
inf = int(1e9)

# 찾아본 솔루션은 함수에 인자를 포함해 두었으나 (함수에서 출력을 위해)
# 전역변수로 사용해도 되기에 삭제
def dijkstra():
    queue = []

    # dijkstra에서 첫 노드의 가중치를 추가하는 부분.
    # (0, 0) 시작이니 이차원 배열에 현재 값을 복사.
    dist[0][0] = graph[0][0]

    # queue에 초기값 삽입
    # queue에 (dist[0][0], 0, 0)을 요소로 추가.
    '''
    < 첫 요소는 무조건 cost >
    - heapq는 첫 번째 요소를 기준으로 정렬을 수행한다.
    - 따라서 '비용'을 기준으로 정렬해야 dijkstra를 구현할 수 있기 때문에 항상 첫 번째 요소가 cost가 된다.
    '''
    heapq.heappush(queue, (dist[0][0], 0, 0))

    # heappush()와 heappop()을 제외하면 일반적인 BFS 다르지 않다.
    while queue:

        '''
        < 우선순위 큐 정리 >
        1. heappop은 우선순위 큐를 기준으로 가장 우선순위가 높은 원소를 반환하다.

        2. 이때 우선순위의 기준은 '튜플'인 경우 '튜플의 첫 번째 원소'가 된다.
            - 현재는 튜플에 (cost, v, h) 순으로 들어가기에 누적 비용합인 cost를 기준으로 우선순위가 적용된다.

        3. 우선순위의 기준은 '작은 값'이 최우선순위를 갖는다.
        '''

        cost, v, h = heapq.heappop(queue)

        '''
        < 로직 정리 >
        1. 인자정리
            - dist[v][h]: 지금까지 탐색한 결과를 기반으로 한 누적 비용합.
            - cost: 같은 좌표인데 이번에 탐색할 때의 누적 비용 합.
        
        2. dist[v][h] < cost
            - 이 조건의 이유는 같은 노드를 여러 번 방문할 수 있는데 이러면 heapq에 같은 노드에 대한 정보가 중복 저장되기 때문에 
            값을 빼 올 때 한번더 비교하여 처리를 해야한다.
            -> 해당 조건이 의미하는 것은 이번에 탐색하는 누적 비용(cost)이 이때까지 탐색한 누적 비용(dist[v][h])보다 작을 경우 탐색한다는 것.
            -> 다익스트라는 최소비용인 경우 업데이트 하고 탐색하기에 당연한 조건.
            -> 이번 탐색이 전 탐색보다 크면 탐색 안하겠다.
        '''
        if dist[v][h] < cost:
            continue

        # 탐색 시작
        for i in range(4):
            nv = v + dv[i]
            nh = h + dh[i]

            # 범위 넘어가면 skip
            if nv < 0 or nv >= N or nh < 0 or nh >= N:
                continue
            
            # 현재까지의 비용에 이동할 곳의 비용을 더함
            temp = cost + graph[nv][nh]

            '''
            < 로직 정리 >
            1. dist가 visited와 유사한 역할을 함.

            2. 현재 누적 비용(temp)이 이동할 공간의 누적 비용(dist[nv][nh])보다 작은 경우에만 heappush함.
                -> 이 말은 dist[nv][nh]를 이미 방문해서 지금까지의 최단비용이 기록 돼 있다면
                -> 새롭게 초기화된 최단비용 temp와 기존의 최단비용 dist[nv][nh]를 비교하고,
                -> 새로운 최단 비용 temp가 더 작다면 dist[nv][nh]를 업데이트한 뒤에 다시 해당 지점을 탐색한다.
            '''
            if temp > dist[nv][nh]:
                continue

            dist[nv][nh] = temp
            # temp가 아니라 'dist[nv][nh]'를 추가해도 결과 동일.
            heapq.heappush(queue, (temp, nv, nh))
        
    # 함수에서 정답 바로 출력
    print(f'Problem {t}: {dist[N-1][N-1]}')

# 몇 번째 문제인지 출력하기 위한 변수 초기화
t = 1

while True:
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # N이 0이면 종료
    if N == 0:
        break

    dist = [[inf] * N for _ in range(N)]
    dijkstra()

    # 다음 문제로 넘어가니 문제도 다음 문제로 초기화
    t += 1
#====================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >

'''

'''
< 시간 복잡도 >

'''

'''
< 문제 정리 >
1. 검은 색 루피를 획득하면 소지한 루피 감소.

2. N * N graph
'''