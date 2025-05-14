import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#======================================================
# 조합 DFS
def DFS(comb = []):

    # comb의 길이가 K와 같아지면 cnt를 +1 하고 반환
    if len(comb) == K:
        ans.append(comb)
        return

    # DFS 선택 로직
    for i in range(N):

        if visited[i]:
            return
        
        visited[i] = True
        DFS(comb + [arr[i]])
        visited[i] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    K = int(input())
    arr = []
    visited = [False] * N
    ans = []

    for i in range(N):
        arr.append(int(input()))

    DFS()
    print(len(ans))
#======================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
- 단순 조합 문제.

- DFS로도 깊이가 4이기에 가능.
'''

'''
< 시간 복잡도 >
- 조합을 구하는 시간 복잡도?

- O(4!)
'''

'''
< 문제 정리 >
1. 카드 4 ~ 10 장
    - 1이상 99이하 정수

2. 카드 2 ~ 4장 선택
    - 가로로 나열
'''