# BFS를 통한 최소 횟수 연산 + visited를 통한 최단 거리
## 백준 1697 - 숨바꼭질
- ‘스타트링크’ 문제와 동일
- BFS를 통해 `최소 횟수` 를 탐색하는 문제.
    - 탐색 문제와 어디가 다름?
        
        → 탐색할 수 있는 범위가 graph로 주어짐. (직관적인 부분)
        
    - 탐색 방법은 어렵지 않음.
        
        → 탐색 경우의 수를 모두 for loop으로 순환하게 하면 됨.
        
        → 이 로직을 BFS로 순환함.
        
        → BFS 자체가 `최단 경로` 혹은 `최소 횟수` 를 보장하기에 가능.
        
    - visited를 통해 방문 체크를 하고, 연산 결과를 출력할 때 `-1` 을 해주어야 한다.

```python
import sys, time
sys.stdin = open('input_1697.txt')
start_time = time.time()

#===========================================
# 탐색을 위한 deque호출
from collections import deque

# 탐색 로직 구현
def BFS(queue):
    while queue:
        start = queue.popleft()

        # 만약 start와 K가 동일하다면 동생을 찾았기 때문에 
        # visited를 출력.
        # 로직에서 설명 했듯이 -1을 해 줌.
        if start == K:
            return visited[start] - 1
        
        '''
        < 핵심 로직 >
        '''
        # 모든 연산 경우를 BFS로 탐색
        for cal_val in (start + 1, start - 1, start * 2):
            
            # 연산의 결과가 범위를 넘으면 skip
            if cal_val < 0 or cal_val > 100000:
                continue

            # 이미 방문하 곳이라면 skip
            if visited[cal_val]:
                continue

            # 위 두 가지 경우가 아니라면 방문 체크 후 탐색 대상에 추가.
            visited[cal_val] = visited[start] + 1
            queue.append(cal_val)
    
    # 탐색을 끝냈음에도 못 찾았다면 못 만나는 것이기에 X를 출력
    return "X"

N, K = map(int, input().split()) # 입력은 간단히 한 줄.
visited = [0] * (100000 + 1) # 전체 그래프 탐색
queue = deque() # 큐 선언

# 수빈이가 시작 node이기에 append
queue.append(N)

# 방문 체크 (방문 체크로인한 1을 이후에 -1로 차감해 주어야 함.)
visited[N] = 1

# 만약 처음부터 같다면 0을 출력하고 아닌 경우에만 BFS를 수행.
if N == K:
    print(0)
else:
    print(BFS(queue))
#===========================================

end_time = time.time()
print('time :', end_time - start_time)

'''
1. 3 가지 로직에 대해 BFS 탐색.

2. 한 줄로 연결된 graph를 세 가지 간선
    
    - +1
    - -1
    - *2
    
    로 탐색.
'''

'''
1. 수빈이의 현재 지점 N
    - 0 <= N <= 100,000

2. 동생의 점 K
    - 0 <= K <= 100,000

3. 수빈이의 이동 로직
    - 한 칸을 이동 (-1 or +1)
    - 순간 이동 (2 * N)
'''
```