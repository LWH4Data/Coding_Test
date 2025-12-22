import sys,time
sys.stdin = open("input.txt")
start = time.time()

#=================================================
# 입력값 받기
N, M = map(int, sys.stdin.readline().split())
# 길이가 M인 수열을 저장할 리스트
S = [0] * M
# 방문여부 리스트
visited = [False] * N

def backtrack(length):
    if length == M:
        # 0부터 처리하기 때문에 마지막 출력 시에는 + 1을 해야한다.
        # join은 문자열에만 사용가능하기에 str을 취한다.
        print(' '.join(str(x + 1) for x in S))
        return
    
    # 모든 노드를 순회
    for i in range(N):

        # 방문 처리 하면서 진행
        if not visited[i]:
            visited[i] = True

            # 가장 마지막에 현재 원소 추가
            S[length] = i
            # 다음 수 추가를 위한 재귀
            backtrack(length + 1)
            # 해당 원소 탐색이 끝났다면 다음 노드 탐색을 위해 반납
            visited[i] = False

backtrack(0)
#=================================================

end = time.time()
print(start - end)