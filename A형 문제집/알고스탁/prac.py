import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#=======================================================
def generate_buy(i, path, remain, price_today, N):
    
    # 입력 받은 값이 마지막 종목인 경우 바로 탐색을 종료하고 path를 list로 반환
    if i == N:
        yield list(path)
        return
    
    # 마지막 종목이 아닌 경우
    # 최대 횟수 = 남은 금액 // 해당 종목의 오늘 가격
    max_cnt = remain // price_today[i]

    # 최대 횟수만큼 순회
    for cnt in range(max_cnt + 1):

        # 구매한 경우의 수에 cnt를 추가.
        path.append(cnt)

        # generate_buy의 결과로 나온 path를 하나씩 반환
        yield from generate_buy(i + 1, path, remain - cnt * price_today[i], price_today, N)

        # 반환한 뒤에는 마지막 경로를 pop
        path.pop()

def DFS(month, Ms, price, N, L, Ma, memo):
    
    # memo에 들어갈 key값 초기화
    # 이번 달에 얼마의 예치금을 들고 있느냐를 key로 한다.
    key = (month, Ms)

    # 만약 이미 key가 있다면 해당 key의 Ms를 반환
    if key in memo:
        return memo[key]
    
    # 모든 기간(month)를 탐색했다면 해당 Ms를 반환
    if month == L:
        return Ms
    
    # DFS 재귀 시작.
    # 아무 주식도 구매하지 않고 넘어가는 경우
    max_profit = DFS(month + 1, Ms + Ma, price, N, L, Ma, memo)
    
    # 전부 구매하지 않은 경우에서 끝 날짜부터 하나씩 구매하는 경우 탐색
    # 오늘 날짜의 종목별 가격을 today로 초기화
    today = price[month]

    # 내일 날짜의 종목별 가격을 tomorrow로 초기화
    tomorrow = price[month + 1]

    # 개별 가격을 순회하며 필요한 변수 계산.
    for buy in generate_buy(0, [], Ms, today, N):
        
        # 특정 종목을 구매하는 데 사용한 비용
        spent = sum(buy[i] * today[i] for i in range(N))

        # 구매하고 남은 비용
        remain = Ms - spent

        # 판매하여 얻을 수익
        sold = sum(buy[i] * tomorrow[i] for i in range(N))

        # 수익을 얻고 남은 금액
        total = remain + sold

        # 수익
        profit = DFS(month + 1, total + Ma, price, N, L, Ma, memo)

        # 최대 수익
        max_profit = max(max_profit, profit)

    # Memoization에 최대 금액을 저장.
    memo[key] = max_profit

    # 최대 금액 반환
    return max_profit 

T = int(input())

for tc in range(1, T + 1):
    Ms, Ma = map(int, input().split())
    N, L = map(int, input().split()) # N: 종목 수 / L: 개월 수
    graph = [list(map(int, input().split())) for _ in range(N)] # [종목][월]

    # 전치를 통해 월별 종목 가격으로 변환
    # (파이썬 list comprehension은 밖의 for loop 부터 수행된다.)
    # 따라서 month가 고정된 상태로 topic 별로 가격을 하나씩 받고, 이를 month로 반복하여 전치를 한다.
    month_price = [[graph[topic][month] for topic in range(N)] for month in range(L + 1)] # [월][종목]으로 변환

    '''
    < Memoization과 DP >: 코테에서는 둘이 같은 의미로 봐도 무방함.
    - Memoization: '재귀 + 캐시'를 통해 함수의 결과를 하나씩 받고 이를 통해 Top-down 방식으로 구현
    - DP: 반복문을 통해 Bottom-up 방식으로 구현.
    '''
    # memoization을 통한 구현
    memo = {}

    result = DFS(0, Ms, month_price, N, L, Ma, memo)
    print(f"#{tc} {result - (Ms + Ma * L)}")
#=======================================================

end_time = time.time()
print('time :', end_time - start_time)