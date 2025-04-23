import sys
sys.stdin = open('input_2798.txt')

T = int(input())

def dfs(index, count, total_sum):
    # rm
    global max_sum
    
    # 3장을 선택했을 때, 합이 M을 넘지 않는 경우 max_sum 갱신
    if count == 3:
        if total_sum <= M:
            max_sum = max(max_sum, total_sum)
        return
    
    # 카드 리스트에서 조합을 만들기 위한 DFS 탐색
    for i in range(index, N):
        dfs(i + 1, count + 1, total_sum + cards[i])  # 다음 카드 선택

# 입력 받기
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 카드 개수 N, 최대 합 M
    cards = list(map(int, input().split()))  # 카드 리스트

    max_sum = 0  # 최댓값 초기화
    dfs(0, 0, 0)  # DFS 탐색 시작

    print(max_sum)  # 결과 출력
