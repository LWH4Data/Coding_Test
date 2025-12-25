import sys, time
sys.stdin = open("input.txt")
start = time.time()

#===================================================
# 종이 데이터를 입력 받는다.
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]

# 색 종이 수 상태구현
#   - index: 색종이, value: 색종이의 수
S = [0, 5, 5, 5, 5, 5]
# 색종이의 최소수를 찾기 때문에 시작은 inf로
result = float('inf')

# 색종이를 붙이는 함수
#   - 색종이에 해당하는 영역(size)를 value로 채운다.
def fill(x, y, size, value):
    for i in range(y, y + size):
        for j in range(x, x + size):
            graph[i][j] = value

# 특정 size의 색종이를 덮을 필요가 있나 확인하는 함수
#   - 최소 색종이 수를 구함을 인지
def check(x, y, size):
    # 해당 size의 색종이 영역을 벗어난다면 False
    if x + size > 10 or y + 10 > 10:
        return False
    
    # 영역 내를 완전 탐색
    for i in range(y, y + size):
        for j in range(x, x + size):
            # 해당 색종이 영역에 1이 아닌 경우가 있다면
            # 해당 색종이를 붙일 필요가 없기에 False
            if graph[i][j] != 1:
                return False
    # 해당 영역이 모두 1이라면 해당 종이를 붙여야 하기에 True
    return True

# 탐색 로직
#   - pos: 이차원 배열을 일차원 배열로 나타냄.
def backtrack(pos, used):
    global result
    # pos == 100인 경우 모든 원소를 본 것.
    # 따라서 종료
    if pos == 100:
        # 탐색이 끝났기에 최소수를 result로 초기화
        result = min(result, used)
        return
    # 결과보다 색종이 사용 수가 더 많다면 종료
    if used >= result:
        return
    # divmod를 통해 pos를 좌표로 환산
    #   - divmod(a, b)
    #       → (a // b, a % b)
    x, y = divmod(pos, 10)
    # 그래프의 해당 영역이 1이라면
    if graph[y][x] == 1:
        # 각 색종이를 순회하면서
        for size in range(5, 0, -1):
            # size에 맞는 색종이가 남아있고, check 필요하다면
            if S[size] > 0 and check(x, y, size):
                # 해당 size의 색종이를 사용하고
                S[size] -= 1
                # 칸을 채운다.
                fill(x, y, size, 0)
                # 이후 반복
                #   - 한 칸 오른쪽으로 이동 및 색종이 사용 상태 전달
                backtrack(pos + 1, used + 1)
                # 백트래킹을 마치고 다음 탐색을 위해 복구
                fill(x, y, size, 1)
                # 색종이 수 복구
                S[size] += 1
    # 색종이 덮을 구역 아니라면 다음 구역으로 넘어가되 색종이 사용은 그대로 전달
    else:
        backtrack(pos + 1, used)

backtrack(0, 0)
# result가 처음 값이 아니면 result 값을, 아니라면 -1을 반환
print(result if result != float('inf') else -1)
#===================================================

end = time.time()
print("time:", start - end)