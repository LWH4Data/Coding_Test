import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==============================================================
"""
완전 탐색 풀이 가능.
"""

def find_order(nth_student: int) -> int:
    """
    각 원소를 모든 수와 비교해서 해당 원소의 순서 찾기.
    """
    
    order = 1

    for i in range(N):
        # 자기 자신과는 비교하지 않음.
        if i == nth_student:
            continue
        
        # 오로지 키와 몸무게 모두 미달일 때에만 등수 + 1
        if students[nth_student][0] < students[i][0] and students[nth_student][1] < students[i][1]:
            order += 1
        # 나머지 경우는 그대로 진행
        else:
            continue
    
    return order

# 입력 받기
N = int(sys.stdin.readline())
students = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    students.append((x, y))

# 순서 리스트에 각 원소의 등수 정보 받기.
order_list = []
for i in range(N):
    order_list.append(find_order(i))

# 출력.
print(*order_list)
#==============================================================

e_t = time.time()
print("time: ", e_t - s_t)