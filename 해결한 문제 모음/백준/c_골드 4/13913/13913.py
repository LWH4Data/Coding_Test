import sys, time 
sys.stdin = open('input_13913.txt')
start_time = time.time()

#==================================================
from collections import deque

# 탐색 델타
dt = (-1, +1, 2)

def BFS(queue):
    while queue:
        start, count, path = queue.popleft()

        # 동생을 찾았다면 값 반환
        if start == K:
            return count, path

        for i in range(3):

            # dt[i] == 2인 경우는 곱 연산
            if dt[i] == 2:
                next = 2 * start
            else:
                next = start + dt[i]

            # 범위 넘으면 skip
            if next < 0 or next > 100000:
                continue

            # 방문 했다면 skip
            if visited[next]:
                continue

            # 둘 다 아니면 방문처리
            visited[next] = True

            # queue에 append + 경로까지
            new_path = path + [next]
            queue.append((next, count + 1, new_path))

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    # 노드가 0 부터 가능하기 때문.
    visited = [False] * 100001

    # 수빈이 위치를 시적점으로
    queue = deque()
    # 경로 받을 리스트 추가
    path = [N]
    count = 0
    queue.append((N, count, path))

    # 방문체크 
    visited[N] = True

    # BFS 탐색
    ans_cnt = 0
    ans_path = []
    ans_cnt, ans_path = BFS(queue)
    print(ans_cnt)
    print(*ans_path)
#==================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
- 수빈이의 위치를 시작점으로 BFS

- 경로를 반환받는다.
'''

'''
< 시간 복잡도 >
1. 하나의 노드마다 세 개의 간선으로 나가기 때문에 O(3^N)
'''

'''
< 문제 정의 >
1. 수빈: 현재 점 N / 동생: K

2. 간선
    2-1. 걷기: 1초 후 X - 1혹은 X + 1 
    2-2. 순간 이동: 1초 후 2*X

3. 시간과 경로를 출력

'''