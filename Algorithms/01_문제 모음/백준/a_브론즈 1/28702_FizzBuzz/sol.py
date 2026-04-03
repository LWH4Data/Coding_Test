import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#===========================================================
cdd = [sys.stdin.readline().strip() for _ in range(3)]

# isdigit()을 통해 정수형 데이터인지 확인하는 풀이.
for i in range(3):
    if cdd[i].isdigit():
        target = int(cdd[i]) + (3 - i)
        break

# 정답 출력
if target % 3 == 0 and target % 5 == 0:
    print("FizzBuzz")
elif target % 3 == 0 and target % 5 != 0:
    print("Fizz")
elif target % 3 != 0 and target % 5 == 0:
    print("Buzz")
else:
    print(target)
#===========================================================

e_t = time.time()
print("time: ", e_t - s_t)