import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

# 3개를 선택하는 완탐시 20 * 20 * 20으로 가능할 듯. 여기에 정렬 Nlog(N)
#==============================================================
# 입력 받기
N = int(sys.stdin.readline())

# 수 리스트 생성
num_list = [0] * (N + 1)
for i in range(1, N + 1):
    num_list[i] = i

# 순열 자료 구조 구현
p_list = []
for i in range(1, N + 1):
    for j in range(2, N + 1):
        for k in range(3, N + 1):
            p_list.append([i, j, k])

# 출력부 구현.
print_list = list(map(int, sys.stdin.readline().split()))
if print_list[0] == 1:
    print(p_list[print_list[1] - 1])

#==============================================================

e_t = time.time()
print("time: ", e_t - s_t)