import sys
sys.stdin = open('input_2798.txt')

T = int(input())

def dfs(index, count, total_sum):
    global max_sum
    
    # 3장을 선택한 경우
    if count == 3:
        if total_sum <= M:
            max_sum = max(max_sum, total_sum)  # 최대값 갱신
        return
    
    # 더 이상 고를 수 있는 카드가 없으면 종료
    if index >= N:
        return

    # 1️⃣ 현재 카드를 선택하는 경우
    dfs(index + 1, count + 1, total_sum + cards[index])

    # 2️⃣ 현재 카드를 선택하지 않는 경우
    dfs(index + 1, count, total_sum)

# 입력 받기
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))

    max_sum = 0  # 최댓값 초기화
    dfs(0, 0, 0)  # DFS 탐색 시작

    print(max_sum)  # 최댓값 출력
