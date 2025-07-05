import sys, time
sys.stdin = open('input_27982.txt')
start_time = time.time()

#================================================
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = deque()

    for i in range(M):
        data.append(list(map(int, input().split())))

    print(data)

    # 5 이하면 애초에 6개 같ㅇ르 수 없으므로 0을 출력
    if len(data) <= 5:
        print(0)

    # 아닌 경우 모든 원소를 완전 탐색
    for sample in data:
        
        i, j, k = sample

        
            


#================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
- queue에 초기 값을 넣고 6가지를 탐색.
'''

'''
< 시간 복잡도 >
- 1회 완탐 5 ^ 3 = 125

- 1회 완탐을 M 번 진행
    -> 125 * 125
    -> 가능.
'''

'''
< 문제 정리 >
1. (i, j, k)의 공간

2. 위의 공간이 M 개 주어짐.

3. M 개의 큐브는 중복되는 일이 없음.

4. (i, j, k), (i +- 1, j, k), (i, j +- 1, k), (i, j, k +- 1) 총 6곳에 큐브가 존재해야 함.
'''