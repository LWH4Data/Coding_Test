import sys,time
sys.stdin = open("input.txt")
start = time.time()

#=================================================
# DFS로 구현
#   - i: 탐색할 전체 N
#   - j: i부터 M개 까지의 조합.
def DFS(i, i + M):
    
    # j가 M을 


# 입력값 받기
N, M = map(int, sys.stdin.readline().split())


print(N, M)
#=================================================

end = time.time()
print(start - end)