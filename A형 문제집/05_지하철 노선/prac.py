import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#===================================================================
# 인접한 역인지를 확인하는 함수
def is_adjacent(i, j, N):

    '''
    < 왜 N으로 나누는가? >
    - 원형 자료 구조이기 때문이다.
    - e.g. 총 10개의 원소가 있을 때 idx = 0과 idx = 0는 인접하다.
        - case 1: (9 - 0) % 10 = 9
        - case 2: (0 - 9) % 10 = 1
            - 파이썬의 %연산은 '음수'를 대상으로 할 경우 '1'이 반환된다.
    - 따라서 원형 자료구조의 끝과 끝의 인접여부를 판단하기위해 N으로 나누는 방법을 활용한다.
    '''
    # 인접한 경우 True, 아닌 경우 False를 반환한다.
    return (i - j) % N == 1 or (j - i) % N == 1

# 간선의 교차여부를 확인하는 함수.


def is_cross(a, b, c, d, N):
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c



T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 지하철 역의 수
    nums = list(map(int, input().split())) # 역마다의 이용객 수

    # 주어진 식의 최댓값을 반환 받기 위해 해당 값을 기록할 변수 초기화
    max_score = 0

    # 가능한 모든 직통 노선 탐색 (완탐)
    for i in range(N):

        # i보다는 1을 크게하여 조합을 탐색
        for j in range(i + 1, N):

            '''
            < 왜 인접여부만 확인하는지? >
            - 첫 번째 연결이기에 '교차(cross)'되는 경우는 존재하지 않는다.
            - 마찬가지로 두 번째 연결이 인접한 노드로 향할지 또한 첫 번째연결이기에 고려하지 않는다.
            '''
            # 인접 여부를 확인하고, 인접하면 skip
            if is_adjacent(i, j, N):
                continue

            # 인접하지 않다면 방문 체크. 매 조합 탐색마다 방문체크를 해야하기에 여기서 visited를 생성.
            visited = [False] * N

            # 연결된 두 노들 체크
            visited[i] = True
            visited[j] = True

            # 연결을 두 번 수행하기 때문에 한 번의 연결을 더 수행한다.
            for k in range(N):
                for l in range(k + 1, N):

                    # 두 번째 연결이기 때문에 다른 조건들도 모두 확인해야 한다.
                    # 1. 인접여부 확인
                    if is_adjacent(k, l, N):
                        continue
                    
                    # 2. 앞서 처리한 방문체크를 통해 중복된 노드에 들어간 경우 skip
                    if visited[k] or visited[l]:
                        continue

                    # 3. 두 간선이 교차 되었다면 skip
                    if is_cross(i, j, k, l, N):
                        continue

#================================================================

end_time = time.time()
print('time :', end_time - start_time)