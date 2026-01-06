import sys, time
sys.stdin = open("input.txt")
start = time.time()

#==================================================
import math
# 에라토스테네스의 체를 활용하여 소수의 제곱근만 체크

# 입력값 받기
A, B = map(int, sys.stdin.readline().split())
# 전체 배열 생성
numbers = [0] * (B + 1)
for i in range(1, B + 1):
    numbers[i] = i

# 소수만 남는 배열 생성.
for i in range(2, int(math.sqrt(B)) + 1):
    for j in range(i + i, B, i):
        numbers[j] = 0

cnt = 0
# 소수의 제곱을 count
for i in numbers:
    if i == 1:
        continue

    if i > B / 2:
        break
    
    for j in range(2, 47):

        if i ** j > B:
            break
        
        if A <= i ** j <= B:
            cnt += 1
            continue
 
print(cnt)
#==================================================

end = time.time()
print("time: ", end - start)