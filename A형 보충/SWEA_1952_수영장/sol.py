import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#======================================================

def solve():
    T = int(input())
    for tc in range(1, T + 1):
        cost_1, cost_1m, cost_3m, cost_1y = map(int, input().split())
        plan = list(map(int, input().split()))
        
        min_cost = cost_1y  # 1년권 기본값

        def dfs(month, total):
            nonlocal min_cost
            if month >= 12:
                min_cost = min(min_cost, total)
                return
            
            # 1. 하루권으로만
            dfs(month + 1, total + plan[month] * cost_1)
            
            # 2. 한달권
            dfs(month + 1, total + cost_1m)
            
            # 3. 3달권
            dfs(month + 3, total + cost_3m)
        
        dfs(0, 0)
        print(f"#{tc} {min_cost}")
solve()
#======================================================

end_time = time.time()
print('time :', end_time - start_time)
