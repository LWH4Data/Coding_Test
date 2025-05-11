import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#=========================================================
from collections import deque

# 탐색 함수
def BFS(start):

    # 시작세팅
    queue = deque()
    queue.append(start)

    while queue:
        start = queue.popleft()
        cnt = 0

        # 동일하게 좌, 우로 한 칸씩 탐색
        flag_0 = True
        while flag_0:
            print(1)
            cnt += 1
            
            # 탐색 시작.
            right = start + cnt
            left = start - cnt

            if (left < 0 or left >= N) and (right < 0 or right >= N):
                flag_0 = False
                return 0
            
            # 범위 조건
            if 0 <= left < N and 0 <= right < N:

                # 만약 양쪽 모두 1이라면 함수 종료하며 0 반환
                if graph[left] == 1 and graph[right] == 1:
                    flag_0 = False
                    return 0
            
                # 아닌 경우 1이 나오면 해당 수 반환
                if graph[left] == 1:
                    ns = left
                    graph[left] = 0
                    flag_0 = False
            
                if graph[right] == 1:
                    ns = right
                    graph[right] = 0
                    flag_0 = False
            
        # queue에 추가.
        queue.append(ns)

    return 0

T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = list(map(int, input().split()))
    flag = True
    dist = 0
    ans = 0

    # 기준점을 기준으로 한 칸씩 멀어지면서 체크
    while flag:
        
        # 우선 첫 번째 거리
        dist += 1

        # 시작 위치 초기화
        # 기준점을 기준으로 좌, 우
        for start in (M + dist, M - dist):

            # 범위 넘어가면 탐색 종료
            if start < 0 or start >= N:
                continue

            # 함수로 최소 거리 반환
            ans = BFS(start)

            # 그대로 0이라면 실패한 것으로 skip
            if ans == 0:
                continue
            
            # 0이 아니면 성공한 것으로 dist 반환 후 while 종료 트리거.
            else:
                print(dist)
                flag = False




    # 시작 인덱스 반복문

    # BFS로 보석 탐색

    # 성공한 경우를 거리에 넣고 마지막에 min으로 반환

#=========================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
1. 기준 칸을 중심으로 주변 영역을 완탐 시작

2. BFS로 돌리면 될 듯.

3. 시뮬
    - 가장 가까운 보석으로 이동
    - 해당 위치에서 가장 가까운 보석의 거리가 같은 경우 end

4. 위의 과정을 반복.

'''

'''
< 시간 복잡도 >
- M을 기준으로 찾는 것이 문제이지 그냥 완탐 돌리면 되니 O(N)

'''

'''
< 문제 정리 >
1. N 칸의 칸이 좌우
-> 일차원 graph

2. 임의 이동, 가장 가까운 보석 차지, 보석 삭제
    - 가장 가까운 보석이 두 개인 경우 보석 가져가지 못함.

3. M 번째 칸
    - 욕심쟁이의 출발 칸을 기준 칸 에서 가장 가까운 곳 위치.
    - 기준 칸에서의 거리 계산

4. 기준 칸과 욕심쟁이 시작 칸은 보석이 없을 수도 있음.
    -> 주어진 기준 칸에서 시작 지점을 탐색.
    -> 만약 전진하다 가까운 보석의 거리가 같다면 end
    -> 이걸 예방하는 시작 위치
    -> 그리고 M과 N의 차이.
'''