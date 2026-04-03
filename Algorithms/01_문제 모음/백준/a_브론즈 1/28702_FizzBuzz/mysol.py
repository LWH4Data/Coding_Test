import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#===========================================================
cdd = []
for _ in range(3):
    cdd.append(sys.stdin.readline().strip())

# 숫자 찾기
check = 0
for i in range(3):
    if cdd[i] != "Fizz" and cdd[i] != "Buzz" and cdd[i] != "FizzBuzz":
        check = i

# diff_val
diff_val = 3 - check
target = int(cdd[check]) + diff_val

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