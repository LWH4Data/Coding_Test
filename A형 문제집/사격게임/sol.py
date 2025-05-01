import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#================================================
# 순열 탐색 DFS
def DFS(depth, visited, path):
    global max_score
    
    # 모든 풍선을 전부 사격한 경우
    # 최대 점수 갱신
    if depth == N:
        max_score = max(max_score, get_score(path))
        return
    
    # 
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            DFS(depth + 1, visited, path + [i])

            # DFS를 탐색하고 난 후에는 복구 시켜줘야 함.
            visited[i] = False


# 점수 계산 함수
def get_score(order):

    # 풍선 리스트를 복사해서 가져온다.
    temp = balloons[ : ]
    
    # 계산 결과를 변수 초기화
    total = 0

    for idx in order:

        # idx 번째 풍선을 터뜨린 경우 점수 구현
        left = idx - 1

        # temp = -1인 경우는 터진 풍선을 의미함.
        # 좌측 풍선 중 터지지 않은 첫 번째 풍선 찾기
        # 우선 바로 왼쪽 확인
        left = idx - 1

        # 왼쪽이 터진 풍선인데 탐색할 풍선이 남은 경우 계속 진행
        while left >= 0 and temp[left] == -1:
            left -= 1

        # 오른쪽 탐색은 왼쪽과 동이
        right = idx + 1
        while right < N and temp[right] == -1:
            right += 1

        # left와 right 모두 풍선이 있는 경우
        if 0 <= left < N and 0 <= right < N and temp[left] != -1 and temp[right] != -1:
            total += temp[left] * temp[right]

        # 왽쪽만 있는 경우
        elif 0 <= left < N and temp[left] != -1:
            total += temp[left]

        # 오른쪽만 있는 경우
        elif 0 <= right < N and temp[right] != -1:
            total += temp[right]

        # 양쪽 모두 없는 경우
        else:
            total += temp[idx]

        # 터진 풍선 체크
        temp[idx] = -1
    
    # 전체 합 반환
    return total
        
T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    balloons = list(map(int, input().split()))
    max_score = 0
    visited = [False] * N
    
    # 탐색 (순열 기반 완전 탐색)
    DFS(0, visited, [])

    # 결과 출력
    print(max_score)
#================================================

end_time = time.time()
print('time :', end_time - start_time)