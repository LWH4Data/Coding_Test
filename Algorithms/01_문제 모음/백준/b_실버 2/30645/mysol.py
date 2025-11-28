import sys, time
sys.stdin = open("input.txt")
start_time = time.time()

#==================================================
T = int(input())

for tc in range(1, T + 1):
    R, C = map(int, input().split())
    N = int(input())
    height = list(map(int, input().split()))

    # 인형을 높이 순서대로 정렬.
    height = sorted(height, reverse=True)

    # 그래프 생성
    graph = [[0] * C for _ in range(R)]

    # 포인터 활용, 인형을 기록하기 위해
    p = 0
    flag = True

    # graph에 인형 적재
    for r in range(R):
        for c in range(C):
            flag = True
            
            # 노드에 적합한 인형 추가.
            while flag:

                # p가 인형의 수보다 커지면 정지.
                if p >= N:
                    break
                
                # 첫 번째 행은 비교 대상이 없기에 그냥 추가.
                if r == 0:
                    graph[r][c] = height[p]
                    flag = False
                    p += 1
                
                # 두 번째 행부터는 이전 행과 비교하여 높이가 같지 않다면 인형을 추가.
                elif r >= 1 and graph[r-1][c] != height[p]:
                    graph[r][c] = height[p]
                    flag = False
                    p += 1
                
                # 위 두 경우가 아니라면 인형을 추가하지 않고 skip
                # 해당 위치에 인형은 적재해야 하기에 while문은 지속
                else:
                    p += 1

    # 중복을 제거하고 인형을 배치하였기에 count만하면 된다.
    Ans = 0
    for r in range(R):
        for c in range(C):
            
            if graph[r][c] == 0:
                continue
            Ans += 1
    print(Ans)
#==================================================

end_time = time.time()
print("time: ", end_time - start_time)

'''
< 시간 복잡도 >
- 정렬: N

- 비교연산: height의 길이 (100,000)

- Ans 연산: R * C
'''

'''
< 로 직 >
- 가장 뒤의 행부터 가장 큰 순서대로 인형이 배치된다.

- 인형을 내림차순으로 정렬하고 graph에 배치를 시작한다.

- 인형을 배치할 때에는 키가 동일한 경우는 skip해야 한다.
    - 이유는 인형의 수가 graph의 크기보다 많은 경우 문제가 되기 때문이다.

- 배치를 완료하였다면 0이 아닌(즉, 인형이 배치된) 칸의 수만 count하면 된다.
'''