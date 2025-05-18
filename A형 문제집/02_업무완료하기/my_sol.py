import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#==================================================
from collections import defaultdict

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    
    # idx로 input을 받는다.
    temp = [0]
    for _ in range(N):
        temp.append(list(map(int, input().split())))

    
    # defaultdict로 그래프 구현
    graph = defaultdict(set)
    for node in range(1, N + 1):
        for child in range(temp[node][1] + 1):
            graph[node].add(temp[node][1 + child])

    print(graph)

#==================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
1. 진입차수가 0인 노드는 무조건 병렬 처리

2. 누구를 도와야할까?
'''

'''
< 시간 복잡도 >

'''

'''
< 문제 정리 >
1. 각각의 업무들은
    - 업무 번호
    - 소요 시간

2. 업무 번호는 1부터 씩 증가.

3. 업무간 독립 혹은 순서 존재.

4. 한 명당 하나의 업무, 병렬처리 가능.
    - 직원 투입 비용 X

5. 김수석은 한 명만 도울 수 있다.
    -> 도와주는 업무의 소요시간은 절반.

6. 입력
    - 소요 시간
    - 완료 업무 목록.

7. 최소 소요시간
    -> 다익?
'''