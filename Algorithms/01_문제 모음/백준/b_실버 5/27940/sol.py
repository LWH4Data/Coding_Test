import sys, time
sys.stdin = open("input.txt")
start_time = time.time()

#========================================================
T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    # 전체 층 수 리스트 생성.
    # 층 수가 index인 리스트를 생성.
    layer = [0] * (N + 1)

    # 비의 정보를 받을 리스트 생성.
    rain = []
    for i in range(M):
        temp = list(map(int, input().split()))
        rain.append(temp)

    # 각 비를 연산하며 첫 번째 값이 K를 초과하는 경우 해당 회차와 index 반환.
    flag = True
    for j in range(M):
        layer[1] += rain[j][1]
        
        # K를 초과한 경우 출력
        if layer[1] > K:
            flag = False
            print(j + 1, 1)
            break
            
    # 초과하는 날이 없는 경우 -1을 출력.
    if flag:
        print(-1)
#========================================================

end_time = time.time()
print("time: ", start_time - end_time)

'''
< 로직 >
- N, M, K
    - N + 1크기의 배열의 생성(인덱스가 층수인 배열)
    - M은 비가 내리는 횟수.
        - 첫 번째 원소의 층까지 두 번째 원소(비의 양)를 누적합.
    - K를 초과하는 층(원소)이 있다면 반복 회수인 i와 max()와 index()를 통해 결과 반환.
'''

'''
< 시간 복잡도 >
- 완탐을 하는 경우 O(M x N)이기에 시간 복잡도가 터진다.
    -> 그리디를 통해 첫 번째 원소만 확인하면 된다.
    -> 그 이유는 일단 1층은 무조건 물이 차이 때문이다.
    -> 이후 index()를 통해 아무 층이나 출력되록 하면 된다.
    -> 이 경우 시간 복잡도는 1층만 비교하기에 O(M)이 된다.
'''

'''
< 문제 정리 >
- 농장은 총 N 층.
    - 1부터 N까지.

- 비는 총 M 번 쏟아진다.
    - i 번째 비가 오면 1층부터 t_i층까지 동시에 빗물을 r_i만큼 받는다.
    - 빗물은 누적.

- 최대 K층 까지 빗물을 받아도 괜찮다.
    - 초과하는 경우 해당 층이 무너진다. (여러 곳도 가능).
'''