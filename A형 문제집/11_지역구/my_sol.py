import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#==============================================================
from collections import defaultdict

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    voters = list(map(int, input().split()))

    # graph를 순회하면서 좌표를 받는다.
    villages = 0
    pos = []
    for v in range(N):
        for h in range(N):
            if arr[v][h] == 1:
                pos.append((v, h))
                villages += 1

    # 좌표대로 graph를 구현하면 양방햔 그래프가 된다.
    graph = defaultdict(set)
    for i in range(villages):
        graph[pos[i][0]].add(pos[i][1])

    


    print(graph)
    break
                



#==============================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >

'''

'''
< 시간 복잡도 >

'''

'''
< 문제 정의 >
1. N 개의 마을
    - 각 마을을 두 개의 지역구로 분리, 대표 선정.

2. 이차원 배열이 재칭으로 주어지는 거 보니
    -> 좌표가 각 노드임.
    -> 좌표를 받고 양방향 그래프로 구현하면 될 듯?
    -> 어차피 최대 400 칸이니 완탐 문제 없음.
'''