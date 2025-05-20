import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#=======================================================
'''
< generate_buy() >
1. 우선 모든 종목을 0주씩 구매한 경우부터 시작한다.

2. DFS가 return되며 가장 마지막 주식부터 현재 남은 금액을 고려하여 1 주씩 구매하는 경우를 고려하며 탐색.

3. 우선 하나의 path(모든 주식 구매 수량)가 완성되면, yield를 반환해 DFS 함수의 for loop을 순회하도록 한다.

4. 다음 조합을 생성하기 위해 generate_buy 함수는 그대로 DFS를 진행.

5. 결국 DFS함수와 generate_buy 함수는 동기화된 방식으로 맞물려 돌아간다.
    - 실제로 병렬은 아니고 맞물려 돌아가는 구조.
'''
def generate_buy(stock_idx, path, remain, price_today):
    
    # 일단 모든 주식에 대한 수량이 결정되면 yield로 반환하여 DFS 함수의 for loop을 수행하게 함.
    # 이후 이 과정을 반복
    if stock_idx == N:
        yield list(path)
        return
    
    # 마지막 종목이 아닌 경우
    # 최대 횟수 = 남은 금액 // 해당 종목의 오늘 가격
    max_cnt = remain // price_today[stock_idx]

    # 현재 주식을 0주부터 최대 수량까지 순회
    for cnt in range(max_cnt + 1):

        # 구매한 경우의 수에 cnt를 추가.
        path.append(cnt)

        # generate_buy의 결과로 나온 path를 하나씩 반환
        yield from generate_buy(stock_idx + 1, path, remain - cnt * price_today[stock_idx], price_today)

        # 다음 조합을 생성하기 위해 현재 종목의 선택 제거
        path.pop()

def DFS(month, Ms):
    global max_profit
    
    # memo에 들어갈 key값 초기화
    # 이번 달에 얼마의 예치금을 들고 있느냐를 key로 한다.
    key = (month, Ms)

    # 만약 이미 key가 있다면 해당 key의 Ms를 반환
    if key in memo:
        return memo[key]
    
    # 모든 기간(month)를 탐색했다면 해당 Ms를 반환
    if month == L:
        return Ms
    
    # 재귀 시작
    # 전부 구매하지 않은 경우에서 끝 날짜부터 하나씩 구매하는 경우 탐색
    # 오늘 날짜의 종목별 가격을 today로 초기화
    today = month_price[month]

    # 내일 날짜의 종목별 가격을 tomorrow로 초기화
    tomorrow = month_price[month + 1]

    # 개별 가격을 순회하며 필요한 변수 계산.햣
    for buy in generate_buy(0, [], Ms, today):
        
        # 특정 종목을 구매하는 데 사용한 비용
        spent = sum(buy[i] * today[i] for i in range(N))

        # 구매하고 남은 비용
        remain = Ms - spent

        # 판매하여 얻을 수익
        sold = sum(buy[i] * tomorrow[i] for i in range(N))

        # 수익을 얻고 남은 금액
        total = remain + sold

        # 수익
        profit = DFS(month + 1, total + Ma)

        # 최대 수익
        max_profit = max(max_profit, profit)

    # Memoization에 최대 금액을 저장.
    memo[key] = max_profit

    # 최대 금액 반환
    return max_profit 

T = int(input())

for tc in range(1, T + 1):
    Ms, Ma = map(int, input().split()) # Ms: 예치금 / Ma: 불입 금액
    N, L = map(int, input().split()) # N: 종목 수 / L: 개월 수
    graph = [list(map(int, input().split())) for _ in range(N)] # [종목][월]

    # 전치를 통해 월별 종목 가격으로 변환
    # (파이썬 list comprehension은 밖의 for loop 부터 수행된다.)
    # 따라서 month가 고정된 상태로 topic 별로 가격을 하나씩 받고, 이를 month로 반복하여 전치를 한다.
    month_price = [[graph[topic][month] for topic in range(N)] for month in range(L + 1)] # [월][종목]으로 변환

    # DFS를 돌면서 최대 수익을 초기화하기위한 변수 초기화
    max_profit = 0

    '''
    < Memoization과 DP >: 코테에서는 둘이 같은 의미로 봐도 무방함.
    - Memoization: '재귀 + 캐시'를 통해 함수의 결과를 하나씩 받고 이를 통해 Top-down 방식으로 구현
    - DP: 반복문을 통해 Bottom-up 방식으로 구현.
    '''
    # memoization을 통한 구현
    memo = {}

    result = DFS(0, Ms)
    print(f"#{tc} {result - (Ms + Ma * L)}")
#=======================================================

end_time = time.time()
print('time :', end_time - start_time)