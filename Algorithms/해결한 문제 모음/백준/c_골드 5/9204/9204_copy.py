import sys, time
sys.stdin = open('input_9204.txt')
start_time = time.time()

#==========================================================
from collections import defaultdict, deque

def solution(games):
    answer = []
    D = [(1, 1), (1, -1), (-1, 1),(-1, -1)] # 퀸의 방향 가중치
    convert = lambda x : chr(x[1] + 65) + ' ' + str(8-x[0]) # row, col을 체스판 형식으로 반환

    for game in games: # test case안에 있는 game
        f, t = (8 - int(game[1]), ord(game[0]) - 65), (8 - int(game[3]), ord(game[2]) - 65)
        Q = deque([(f, 0, convert(f))]) # location, count, path
        visited = [[0]*8 for _ in range(8)] # 방문 표시
        visited[f[0]][f[1]] = 1 # 시작 칸 
        ans = 'Impossible' # 목적지 't'에 갈 수 없다면 Impossible 반환

        while Q: # BFS
            cur, count, path = Q.popleft()
            if cur == t: # 목적지 도달
                ans = str(count) + ' ' + path
                break

            for d in D: # 방향에 따라 갈 수 있는 모든 칸 탐색
                next_cur = cur # 탐색 칸
                while True: # 같은 방향, 여러칸 이동 탐색
                    next_cur = (next_cur[0] + d[0], next_cur[1] + d[1])
                    if not (0 <= next_cur[0] < 8) or not (0 <= next_cur[1] < 8): # 체스판 벗어남
                        break
                    if visited[next_cur[0]][next_cur[1]] == 0: # 처음 방문하는 칸만 push
                        visited[next_cur[0]][next_cur[1]] = 1
                        Q.append((next_cur, count + 1, path + ' ' + convert(next_cur)))

        answer.append(ans)

    return '\n'.join(answer)

if __name__ == '__main__':
    T = int(input())
    games = []
    for _ in range(T):
        games.append(input().split())
    result = solution(games)
    print(result)
#==========================================================

end_time = time.time()
print('time :', end_time - start_time)