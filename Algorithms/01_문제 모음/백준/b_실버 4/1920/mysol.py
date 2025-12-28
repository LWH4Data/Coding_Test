import sys, time
sys.stdin = open("input.txt")
start = time.time()

#==============================================
# 입력 받기
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

# 이진 탐색을 위해 정렬
numbers.sort()

# 탐색 시작
for i in range(M):
    start = 0
    end = N - 1
    
    # 같지 않을 동안 반복
    while end - start != 1:
        # print("start: ", start, "end: ", end, "i: ", i, "target: ", targets[i])
        
        # 끝점 예외 처리
        if numbers[0] == targets[i]:
            print(1)
            break
        elif numbers[N-1] == targets[i]:
            print(1)
            break

        # 중앙값 찾기
        # 찾았다면 1을 출력
        mid_idx = (start + end) // 2

        # 중앙값 비교 로직
        if numbers[mid_idx] == targets[i]:
            print(1)
            break

        if numbers[mid_idx] < targets[i]:
            start = mid_idx 

        if numbers[mid_idx] > targets[i]:
            end = mid_idx
    
    # 찾지 못한 경우는 0 출력
    if end - start == 1:
        print(0)
#==============================================

end = time.time()
print("time:", start - end)