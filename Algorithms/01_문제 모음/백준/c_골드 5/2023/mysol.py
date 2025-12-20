import sys, time
sys.stdin = open("input.txt")
start = time.time()

#==========================================================
# DFS 함수
def DFS(nth):

    # 자리수를 넘는다면 끝.
    if nth == -1:
        return 
    
    # 확인할 수를 초기화
    check_num = number // 10**nth

    # 소수인지 탐색
    for i in range(10**(N-nth), 10**(N+1-nth)):
        
        # 만약 i로 나뉘어 떨어지면 안됨.
        if i != 1 and check_num % i == 0:
            return

        # 위의 조건에 걸리지 않으면 DFS
        nth -= 1
        print(check_num, nth)
        # DFS(nth)
    
    # 모든 수를 순회한 결과면 append
    if nth == 0:
        ans.append(number)
    

# 입력값 받기
N = int(sys.stdin.readline())
ans = []

# 자리수의 모든 수를 순회
for number in range(10**N, 10**(N+1)):
    nth = N
    DFS(nth)

print(ans)

# DFS로 각 자리수를 더해 소수인지 판단

# 중간에 끊기면 return을 하고 함수 종료.

# 끊기지 않고 모든 DFS를 완수 했다면 ans에 append
#==========================================================

end = time.time()
print("time:", start - end)