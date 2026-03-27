import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#===============================================================
"""
6의 배수의 누적합 만큼 벌집의 수가 증가한다.
따라서 누적합 보다 주어진 N이 처음으로 작아지는 시점이 거리가 된다.
"""
# 입력 받기.
N = int(sys.stdin.readline())

t = 0
checkpoint = 1

while checkpoint < N:

    # 누적합을 반복
    checkpoint += 6 * t

    # t를 증가.
    t += 1

if N == 1:
    print(1)
else:
    print(t)
#===============================================================

e_t = time.time()
print("time: ", e_t - s_t)